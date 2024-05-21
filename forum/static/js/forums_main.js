/** construye consulta */
const buildQueryString = (params) => {
    return Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');
};


/** obtiene los foros */
const fetch_forums = async (params) => {
    try{
        const url = `/api/forums?${buildQueryString(params)}`;
        const response = await fetch(url);
        return response.json();
    } catch (error) {
        throw new Error('Error al obtener los foros');
    }
};

let params = {};
/** escucha el evento de cambio de titulo */
document.getElementById('search-title').addEventListener('input', (event) => {
    let forums = document.getElementById('forums-container');
    params.title = event.target.value;

    /** get all the forums */
    fetch_forums(params).then((data) => {
        /** clean the forums innerhtml */
        forums.innerHTML = '';
        data.forEach(element => {
            /** for each, append to the forums list */
            forums.innerHTML += 
                `<a id="forum-entry" class="forum-entry" href="/forum/${element.id}">
                    <div class="entry-data">
                        <div> Votos: +${5} </div>
                        <div> Respuestas: ${10} </div>
                    </div>
                    <div class="entry-content">
                        <div class="entry-title"> ${element.title} </div>
                        <div class="entry-body">  ${element.body} </div>
                    </div>  
                </a>`;
        });

    });

});

