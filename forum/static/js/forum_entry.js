forum_id = window.location.pathname.split('/')[2];
console.log(forum_id)

const fetch_forum = async (id) => {
    try{
        const url = `/api/forums/${id}`;
        const response = await fetch(url);
        return response.json();
    } catch (error) {
        throw new Error('Error al obtener el foro');
    }
}




