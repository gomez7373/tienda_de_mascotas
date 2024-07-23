// static/js/login.js
// Maneja la lógica del formulario de inicio de sesión

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        if (data.error) {
            responseDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            responseDiv.innerHTML = `<p style="color: green;">Inicio de sesión exitoso. Bienvenido, ${data.name} ${data.surname}.</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
