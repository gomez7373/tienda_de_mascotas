// static/js/payment.js
// Maneja la lógica del formulario de pago

document.getElementById('paymentForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario

    const user_id = document.getElementById('user_id').value;
    const amount = document.getElementById('amount').value;

    fetch('/pay', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: user_id, amount: amount })
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        if (data.error) {
            responseDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            responseDiv.innerHTML = `<p style="color: green;">Pago exitoso por ${amount} unidades monetarias.</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
