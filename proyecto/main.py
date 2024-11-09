from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import json
from datetime import datetime

app = FastAPI()

# Agregar soporte para sesiones
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.mount("/static", StaticFiles(directory="static"), name="static")

def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

@app.get("/", response_class=HTMLResponse)
async def login_page():
    with open("static/login.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/check-in", response_class=HTMLResponse)
async def check_in_page(request: Request):
    if not request.session.get("user"):
        return RedirectResponse(url="/")
    with open("static/check_in.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...), request: Request = None):
    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            request.session["user"] = user
            return RedirectResponse(url="/check-in", status_code=302)
    raise HTTPException(status_code=401, detail="Credenciales incorrectas.")

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

@app.post("/check-in")
async def check_in(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    users = load_users()
    for u in users:
        if u["email"] == user["email"]:
            u["check_in"] = datetime.now().isoformat()
            save_users(users)
            return {"message": "Check-in exitoso"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.post("/check-out")
async def check_out(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no autenticado")
    users = load_users()
    for u in users:
        if u["email"] == user["email"]:
            u["check_out"] = datetime.now().isoformat()
            save_users(users)
            return {"message": "Check-out exitoso"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
