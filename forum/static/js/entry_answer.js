// Encuentra el botón "Responder" por su ID
var answerButton = document.getElementById('answer-button');
var formRespuesta = document.getElementById('form-respuesta');
// Añade un controlador de eventos para el clic en el botón "Responder"
answerButton.addEventListener('click', function() {
    // Encuentra el formulario de respuesta por su ID
    
    // Verifica si el formulario está oculto o visible y cambia su estado
    if (formRespuesta.hasAttribute('hidden')) {
        formRespuesta.removeAttribute('hidden'); // Muestra el formulario
    } else {
        formRespuesta.setAttribute('hidden', true); // Oculta el formulario
    }
});

