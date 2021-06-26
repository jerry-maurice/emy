const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const navItem = document.getElementsByClassName('nav-item');
const navItemLength = navItem.length;    
const section_list = ['homePage','aboutPage','committeePage','eventsPage','contactSection','memberPage'];                      

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

//navigation - section selection
for(let i=0;i<navItemLength;i++){
    navItem[i].addEventListener('click', function(){
        const section_id = document.getElementById(section_list[i]);
        if(i!=5){
            section_id.scrollIntoView({
                behavior:'smooth'
            });
        }
        else{
            //redirect to member page if authenticated
            //window.location.href = '/login/auth0';
            window.location.href = '/member/home';
        }
        
    })
}