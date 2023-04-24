const navbar = document.querySelector(".navbar");
const close =  document.querySelector(".close");
const show_navbar = document.querySelector(".show_navbar");
const show_menu = document.querySelector(".drop_down_menu_button");

const menu_container = document.querySelector(".menu_overall");

const menu = document.querySelector(".menu");

document.addEventListener("click" , (event)=>{
    if(!menu_container.contains(event.target)){
        menu.removeAttribute("style");
    }
})

show_navbar.addEventListener("click" , ()=>{
    navbar.style.left = "0px";
});

close.addEventListener("click" , ()=>{
    navbar.removeAttribute("style");
});

show_menu.addEventListener("click" , ()=>{
    menu.style.display = "flex"
})

