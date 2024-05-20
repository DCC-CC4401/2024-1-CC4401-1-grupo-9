const forum_id = window.location.pathname.split('/')[2];

const fetch_forum = async (id) => {
    try{
        const url = `/api/forums/?entry_id=${id}`;
        const response = await fetch(url);
        return response.json();
    } catch (error) {
        throw new Error('Error al obtener el foro');
    }.0
}

fetch_forum(forum_id).then((data) => {
    document.getElementById('entry').innerHTML = 
        `<div class="entry">
            <div class="entry-data">
                <div> Votos: +${5} </div>
                <div> Respuestas: ${10} </div>
            </div>
            <div class="entry-content">
                <div class="entry-title">${data.forum.title} </div>
                <div class="entry-body">${data.forum.body} </div>
            </div>
        </div>`;

    for (let i = 0; i < data.messages.length; i++) {
        document.getElementById('entry-answer').innerHTML += 
            `<div class="entry">
                <div class="entry-content">
                    <div class="entry-message"> ${data.messages[i].message} </div>
                </div>
                <div class="entry-data">
                    <div> Votos: +${5} </div>
                    <div> Respuestas: ${10} </div>
                </div>
            </div>`;
    }
});
 



