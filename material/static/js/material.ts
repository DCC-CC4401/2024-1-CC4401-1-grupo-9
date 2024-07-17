
const comments: HTMLElement | null = document.getElementById('comments') as HTMLElement || null;

const button: HTMLElement | null = document.getElementById('response-button') as HTMLElement || null;
const response: HTMLTextAreaElement | null = document.getElementById('response') as HTMLTextAreaElement || null;


const handleComment = (_: Event) => { 
    if(!response || response.value === '') return;

    const msg: string = response?.value || '';
    response.value = '';

    if(comments){
        comments.innerHTML = `
            <div class="comment">
                <div class="text"> ${msg} </div>
                <div class="response-button"> Responder </div>
            </div> 
            ` + comments.innerHTML;
    }
};

button?.addEventListener('click', handleComment);














