const DISCOVERING_MEMBERS = '/discovering';

document.addEventListener('DOMContentLoaded',()=>{
    getMembersRecommendation(DISCOVERING_MEMBERS);
} );

const getMembersRecommendation = async (DISCOVERING_MEMBERS)=>{
    const res = await fetch(DISCOVERING_MEMBERS, {
        method:'GET', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    try{
        const data = await res.json();
        displayMembers((data));
    }catch(error){
        console.log("error", error)
    }
}

function displayMembers(data){
    let follower = document.getElementById('follower');
    let following = document.getElementById('following');
    console.log(data.follower);
    follower.textContent = (data.follower);
    following.textContent = (data.following);

    /*
    let data = JSON.parse(members.members);
    console.log(data.length);
    for (const member of (data)){
        detail = member.fields;
        let user_div = document.createElement('div');
        user_div.classList.add('card');

        let user_image = document.createElement('img');
        let user_name = document.createElement('p');
        let user_link = document.createElement('a');

        user_name = document.createTextNode(detail.user.username);
        user_image.src=detail.image.url;
        user_div.appendChild(user_name);

        myDocFrag.appendChild(user_div);
    }
    div_recommendation.appendChild(myDocFrag);*/
}