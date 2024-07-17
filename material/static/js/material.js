"use strict";
const comments = document.getElementById('comments') || null;
const button = document.getElementById('response-button') || null;
const response = document.getElementById('response') || null;
const handleComment = (_) => {
    if (!response || response.value === '')
        return;
    const msg = (response === null || response === void 0 ? void 0 : response.value) || '';
    response.value = '';
    if (comments) {
        comments.innerHTML = `
            <div class="comment">
                <div class="text"> ${msg} </div>
                <div class="response-button"> Responder </div>
            </div> 
            ` + comments.innerHTML;
    }
};
button === null || button === void 0 ? void 0 : button.addEventListener('click', handleComment);
