
//********************menú responsivo****************** */
// Con esta funcion al hacer click se llama al menú oculto de css y html
const navToggle=document.querySelector(".nav_toggle")
const navMenu=document.querySelector(".nav-menu")




navToggle.addEventListener("click",()=>{
    navMenu.classList.toggle("nav-menu_visible")





//*********************************************************** */



// con el siguiente if hacemos que la página se pueda usar con el tabulador
    if (navMenu.classList.contains("nav-menu_visible")){
        navToggle.setAttribute("aria-label","Cerrar menú");
    } else{
        navToggle.setAttribute("aria-label","Abrir Menú");
    }

})


//*********************************************************** */
// Carrousel

let slideIndex = 1;
showSlides(slideIndex)

function plusSlides(n){
    showSlides(slideIndex += n)
}
function currentSlide(n){
    showSlides(slideIndex = n);
}
function showSlides(n){
    let i;
    let slides = document.querySelectorAll(".mySlides");
    let quadrates = document.querySelectorAll(".quadrate");
    
    if(n > slides.length) slideIndex = 1
    if(n < 1) slideIndex = slides.length
    for(i = 0; i < slides.length; i++){
        slides[i].classList.replace("activef","disNone")
    }
    for(i = 0; i < quadrates.length;i++){
        quadrates[i].className = quadrates[i].className.replace("activeC","")
    }

    slides[slideIndex-1].classList.replace("disNone","activef")
    quadrates[slideIndex-1].className += " activeC";
    

}


let slideIndexT = 1;
function currentSlideT(m){
    tallas(slideIndexT = m)
}
let tallas = function(m){
    let i;
    let tallas = document.querySelectorAll(".tallas__container--item") 
    if(m > tallas.length) slideIndexT = 1
    if(m < 1) slideIndexT = tallas.length
    for(i=0; i<tallas.length ;i++){
        tallas[i].className = tallas[i].className.replace("tallaActive","")
    }
    tallas[slideIndexT-1].className += " tallaActive";
} 



let slideIndexP = 1

function currentSlideP(o){
    hover(slideIndexP = o);
}


let hover = function(o){
    let i;
    let quadratesP = document.querySelectorAll(".quadrate--p");
    if(o > quadratesP.length) slideIndexP = 1
    if(o < 1) slideIndexP = quadratesP.length
    for(i = 0; i < quadratesP.length; i++){
        quadratesP[i].classList.remove("disActivP")
    }
    quadratesP[slideIndexP-1].classList.add("disActivP");
}


