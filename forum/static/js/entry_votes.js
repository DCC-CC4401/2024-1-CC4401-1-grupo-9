const entry_id = window.location.pathname.split('/')[2];

const downvoteButton = document.getElementById('downvote');
const upvoteButton = document.getElementById('upvote');
const spanVotes = document.getElementById('votes-counter');
const entry_votes = document.getElementById('entry-votes');


downvoteButton.addEventListener('click', async() => {
    const formData = new FormData();
    formData.append('vote', -1);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = `/api/vote/?entry_id=${entry_id}&vote_type=0`;
    const response = await fetch(url, {method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData});
    const data = await response.json();
    spanVotes.textContent = data.total_votes;
    entry_votes.textContent = "Votos:" + data.voter_count;
});

upvoteButton.addEventListener('click', async() => {
    const formData = new FormData();
    formData.append('vote', 1);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const url = `/api/vote/?entry_id=${entry_id}&vote_type=0`;
    const response = await fetch(url, {method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData});
    const data = await response.json();
    spanVotes.textContent = data.total_votes;
    entry_votes.textContent = "Votos:" + data.voter_count;
});


