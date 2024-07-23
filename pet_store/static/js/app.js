// static/js/app.js
// Maneja la lógica general de la aplicación en el lado del cliente

document.addEventListener('DOMContentLoaded', (event) => {
    // Este código se ejecutará cuando el DOM esté completamente cargado

    // Ejemplo de cómo manejar un clic en un botón
    const exampleButton = document.getElementById('exampleButton');
    if (exampleButton) {
        exampleButton.addEventListener('click', () => {
            alert('Button clicked!');
        });
    }
    
    // Puedes añadir más lógica y manejadores de eventos aquí
});
