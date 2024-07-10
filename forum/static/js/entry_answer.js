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

// Añade un controlador de eventos para el evento de envío del formulario
formRespuesta.addEventListener('submit', function(event) {
    event.preventDefault(); // Previene el envío predeterminado del formulario

    const entry_id = window.location.pathname.split('/')[2];
    const message = document.getElementById('answer-text').value;

    const formData = new FormData();
    formData.append('message', message);

    // CSRF token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    

    fetch(`/api/forums/?entry_id=${entry_id}`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData
    })
    .then(response => {
        if(response.ok) {
            return response.json(); // o response.text() si esperas una respuesta en texto plano
        }
        throw new Error('Algo salió mal con la petición fetch.');
    })
    .then(data => {
        console.log(data);
        window.location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
    });
});