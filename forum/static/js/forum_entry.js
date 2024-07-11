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
    fetch_votes(forum_id).then((votes) => {
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
        p.textContent = data.forum.body;
        entry_body.appendChild(p);

        entry_answer = document.getElementById('entry-answers');
        p = document.createElement('p');
        p.textContent = "Respuestas:" + data.messages.length;
        entry_answer.appendChild(p);

        const entry_votes = document.getElementById('entry-votes');
        p = document.createElement('p');
        p.textContent = "Votos:" + votes.entry_votes_count;
        entry_votes.appendChild(p);

        votes_counter = document.getElementById('votes-counter');
        votes_counter.textContent = votes.entry_votes[forum_id];

        document.getElementById('num-answers').innerText = "Respuestas: " + data.messages.length;

        /* *********************************************************************

            Recuperacion de mensajes y sistema de votos para cada mensaje
        
        
        ********************************************************************* */

        const answerContainer = document.getElementById('answer-container'); 

        for (let i = 0; i < data.messages.length; i++) {
            const answerDiv = document.createElement('div');
            answerDiv.className = 'answers';

            const authorTimeDiv = document.createElement('div');
            authorTimeDiv.className = 'answer-author-time';
            const authorTimeP = document.createElement('p');
            authorTimeP.textContent = `Respondido por ${data.messages[i].user} hace ${date_timeCalculator(data.messages[i].created_at)}`;
            authorTimeDiv.appendChild(authorTimeP);

            const contentDiv = document.createElement('div');
            contentDiv.className = 'answer-content';
            const contentP = document.createElement('p');
            contentP.className = 'answer-content';
            contentP.textContent = data.messages[i].message;
            contentDiv.appendChild(contentP);

            const buttonsDiv = document.createElement('div');
            buttonsDiv.className = 'answer-buttons';

            const buttonUp = document.createElement('button');
            buttonUp.className = 'button-up';
            buttonUp.textContent = 'Upvote';
            buttonUp.id = `button-up-${data.messages[i].id}`;

            const votesSpan = document.createElement('span');
            votesSpan.textContent = votes.message_votes[data.messages[i].id];

            const buttonDown = document.createElement('button');
            buttonDown.className = 'button-down';
            buttonDown.textContent = 'DownVote';
            buttonDown.id = `button-down-${data.messages[i].id}`;

            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            // Agregar EventListeners
            buttonUp.addEventListener('click', async () => {
                const formData = new FormData();
                formData.append('vote', 1);
                const message_data = await fetch_forum(forum_id);
                const url = `/api/vote/?entry_id=${forum_id}&message_id=${message_data.messages[i].id}&vote_type=1`;
                const body = formData;
                const response = await fetch(url, {method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: body});
                const data = await response.json();
                votesSpan.textContent = data.total_votes;
                
            });

            buttonDown.addEventListener('click', async () => {
                const formData = new FormData();
                formData.append('vote', -1);
                const message_data = await fetch_forum(forum_id);
                const url = `/api/vote/?entry_id=${forum_id}&message_id=${message_data.messages[i].id}&vote_type=1`;
                const response = await fetch(url, {method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData});
                const data = await response.json();
                votesSpan.textContent = data.total_votes;
            });

            buttonsDiv.appendChild(buttonDown);
            buttonsDiv.appendChild(votesSpan);
            buttonsDiv.appendChild(buttonUp);


            answerDiv.appendChild(authorTimeDiv);
            answerDiv.appendChild(contentDiv);
            answerDiv.appendChild(buttonsDiv);

            answerContainer.appendChild(answerDiv);
        }
    });
});

            
            