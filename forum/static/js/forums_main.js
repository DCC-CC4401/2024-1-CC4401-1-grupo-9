
/** construye consulta */
const buildQueryString = (params) => {
    return Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
};


let params = {};
/** escucha el evento de cambio de titulo */
document.getElementById('search-title').addEventListener('input', async (event) => {
    const forums = document.getElementById('forums-container');
    params.title = event.target.value;

    const url = `/api/forums?${buildQueryString(params)}`;
    fetch(url)
        .then(response => response.json())
        .then((data) => {
        /** clean the forums innerhtml */
        forums.innerHTML = '';
        data.forEach(element => {
            /** for each, append to the forums list */
            forums.innerHTML += 
                `<a id="forum-entry" class="forum-entry" href="/forum/${element.id}">
                    <div class="entry-content">
                        <div class="entry-title"> ${element.title} </div>
                        <div class="entry-body">  ${element.body} </div>
                    </div>  
                </a>`;
        });
    });
});



const textArea = document.getElementById("entry-form-body");
textArea.addEventListener("input", _ => {
    textArea.style.height = "auto";
    const height = Math.max(textArea.scrollHeight, 150);
    textArea.style.height = `${height}px`;
});

