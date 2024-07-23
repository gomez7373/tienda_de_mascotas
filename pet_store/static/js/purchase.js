// static/js/purchase.js
// Maneja la lógica del formulario de compra

document.getElementById('purchaseForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario

    const animal = document.getElementById('animal').value;
    const quantity = document.getElementById('quantity').value;
    const user_id = 1;  // Ejemplo: ID de usuario fijo, debe ser dinámico en una aplicación real

    fetch('/buy', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: user_id, animal: animal, quantity: quantity })
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        if (data.error) {
            responseDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            responseDiv.innerHTML = `<p style="color: green;">Compra exitosa: ${quantity} ${animal}(s) comprados.</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
