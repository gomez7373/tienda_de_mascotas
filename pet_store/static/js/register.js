// static/js/register.js
// Maneja la lógica del formulario de registro

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const name = document.getElementById('name').value;
    const surname = document.getElementById('surname').value;

    fetch('/users/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password, name: name, surname: surname })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/users/login';  // Redirigir al usuario a la página de inicio de sesión
        } else {
            const responseDiv = document.getElementById('response');
            responseDiv.innerHTML = `<p style="color: red;">Error en el registro.</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
