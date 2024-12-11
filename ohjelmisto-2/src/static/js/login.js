function switchTab(tab) {
    const registerForm = document.getElementById('registerForm');
    const loginForm = document.getElementById('loginForm');
    const tabs = document.querySelectorAll('.tab');

    if (tab === 'register') {
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
        tabs[0].classList.add('active');
        tabs[1].classList.remove('active');
    } else {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
        tabs[0].classList.remove('active');
        tabs[1].classList.add('active');
    }
}

async function createAccount() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const messageDiv = document.getElementById('registerMessage');

    try {
        const response = await fetch('/create_account', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        messageDiv.textContent = data.message;
        messageDiv.className = `message ${data.success ? 'success' : 'error'}`;

        if (data.success) {
            localStorage.setItem('username', data.username);
            setTimeout(() => {
                window.location.href = '/main_menu';
            }, 1500);
        }
    } catch (error) {
        messageDiv.textContent = 'An error occurred. Please try again.';
        messageDiv.className = 'message error';
    }
}

async function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const messageDiv = document.getElementById('loginMessage');

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        messageDiv.textContent = data.message;
        messageDiv.className = `message ${data.success ? 'success' : 'error'}`;

        if (data.success) {
            localStorage.setItem('username', data.username);
            setTimeout(() => {
                window.location.href = '/main_menu';
            }, 1500);
        }
    } catch (error) {
        messageDiv.textContent = 'An error occurred. Please try again.';
        messageDiv.className = 'message error';
    }
}