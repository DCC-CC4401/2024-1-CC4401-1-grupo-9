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

fetch_forum(forum_id).then((data) => {
    title = document.getElementById('entry-title');
    h2 = document.createElement('h2');
    h2.innerHTML = data.forum.title;
    title.appendChild(h2);

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
 


