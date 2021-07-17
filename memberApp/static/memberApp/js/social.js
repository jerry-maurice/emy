const likeUrl = "/social/likes/";

//fetch number of like
let numberOfLikes = document.getElementById('numberLikes');
let numberOfComments = document.getElementById('numberComments');

function retrieveLikes(id){
    fetch(likeUrl+id,{
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => {
        return response.json();
    })
    .then(data =>{
        numberOfLikes.textContent = data.likes;
        numberOfComments.textContent = data.comments;
    })
}

//add like
function addLike(id){
    fetch(likeUrl+id, {
        method: 'POST',
        credentials: 'same-origin',
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
    },
        body: JSON.stringify({'post_data':'Data to post'}) //JavaScript object of data to POST
    })
    .then(response => {
          return response.json() //Convert response to JSON
    })
    .then(data => {
    //Perform actions with the response data from the view
        retrieveLikes(id);
    })
}

//display comment
function addComment(){
    let commentForm = document.getElementById("new-comment");
    commentForm.classList.toggle('new-comment-hide');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');