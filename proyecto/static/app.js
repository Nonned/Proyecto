document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById('login-form');
    const checkInBtn = document.getElementById('check-in-btn');
    const checkOutBtn = document.getElementById('check-out-btn');
    const logoutBtn = document.getElementById('logout-btn');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            if (response.redirected) {
                window.location.href = response.url;
            } else if (response.status === 401) {
                alert('Credenciales incorrectas.');
            } else {
                alert('Error inesperado. Intenta nuevamente.');
            }
        });
    }

    if (checkInBtn) {
        checkInBtn.addEventListener('click', async () => {
            const response = await fetch('/check-in', { method: 'POST' });
            if (response.ok) {
                alert('Check-in exitoso.');
                checkInBtn.classList.add('d-none');
                checkOutBtn.classList.remove('d-none');
            }
        });
    }

    if (checkOutBtn) {
        checkOutBtn.addEventListener('click', async () => {
            const response = await fetch('/check-out', { method: 'POST' });
            if (response.ok) {
                alert('Check-out exitoso.');
                checkInBtn.classList.remove('d-none');
                checkOutBtn.classList.add('d-none');
            }
        });
    }

    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            await fetch('/logout', { method: 'POST' });
            window.location.href = '/';
        });
    }
});
