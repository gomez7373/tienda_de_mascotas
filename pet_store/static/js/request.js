// static/js/request.js
// Maneja la lógica del formulario de solicitud de animales

document.getElementById('requestForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario

    const user_id = document.getElementById('user_id').value;
    const animal_name = document.getElementById('animal_name').value;
    const phone = document.getElementById('phone').value;

    fetch('/animals/request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: user_id, animal_name: animal_name, phone: phone })
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        if (data.success) {
            responseDiv.innerHTML = `<p style="color: green;">${data.message}</p>`;
        } else {
            responseDiv.innerHTML = `<p style="color: red;">Error al registrar la solicitud.</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
