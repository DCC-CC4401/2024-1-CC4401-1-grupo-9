const forum_id = window.location.pathname.split('/')[2];

const fetch_forum = async (id) => {
    try{
        const url = `/api/forums/?entry_id=${id}`;
        const response = await fetch(url);
        return response.json();
    } catch (error) {
        throw new Error('Error al obtener el foro');
    }
}

const fetch_votes = async (id) => {
    try{
        const url = `/api/vote/?entry_id=${id}`;
        const response = await fetch(url);
        return response.json();
    } catch (error) {
        throw new Error('Error al obtener los votos');
    }
}

function date_timeCalculator(datetime){
    const date = new Date(datetime);
    const now = new Date();
    const diff = now - date;

    const seconds = Math.floor(diff / 1000);
    const minutes = Math.floor(seconds / 60);
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);
    const months = Math.floor(days / 30);
    const years = Math.floor(months / 12);

    if (years > 0) return years + " años";
    if (months > 0) return months + " meses";
    if (days > 0) return days + " días";
    if (hours > 0) return hours + " horas";
    if (minutes > 0) return minutes + " minutos";
    if (seconds > 0) return seconds + " segundos";
    return "0 segundos";
}

fetch_forum(forum_id).then((data) => {
    title = document.getElementById('entry-title');
    h2 = document.createElement('h2');
    h2.textContent = data.forum.title;
    title.appendChild(h2);

    entry_author_time = document.getElementById('entry-author-time');
    p = document.createElement('p');
    p.textContent = `Subido por ${data.forum.user} hace ${date_timeCalculator(data.forum.created_at)}`;
    entry_author_time.appendChild(p);

    entry_body = document.getElementById('entry-body');
    p = document.createElement('p');
    p.innerHTML = data.forum.body;
    entry_body.appendChild(p);

    document.getElementById('num-answers').innerText = "Respuestas: " + data.messages.length;


    /* ${data.forum.body} */


    for (let i = 0; i < data.messages.length; i++) {
        document.getElementById('answer-container').innerHTML += 
        `<div id="answers" class="answers">
            <div id="answer-author-time" class="answer-author-time">
                <p> Subido por Usuario Genérico2 hace 2 horas </p>
            </div>
            <div id="answer-content" class="answer-content"> 
                <p class="entry-message"> ${data.messages[i].message} </p>
            </div>
            <div id="answer-buttons" class="answer-buttons">
                <button id="upvote" class="upvote"> Upvote </button>
                <span class="votes-counter"> +1 </span>
                <button id="downvote" class="downvote"> Downvote </button>
            </div>
        </div>`;
    }
});
 



