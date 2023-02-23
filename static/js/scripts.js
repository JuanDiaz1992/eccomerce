
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
    let radio = document.querySelectorAll(".colorSection");
    
    if(n > slides.length) slideIndex = 1
    if(n < 1) slideIndex = slides.length
    for(i = 0; i < slides.length; i++){
        slides[i].classList.replace("activef","disNone")
        
    }
    for(i = 0; i < quadrates.length;i++){
        quadrates[i].className = quadrates[i].className.replace("activeC","")

    }
    for(i = 0; i < radio.length;i++){
        radio[i].checked = radio[i].checked=false
    }

    slides[slideIndex-1].classList.replace("disNone","activef")
    quadrates[slideIndex-1].className += " activeC";
    radio[slideIndex-1].checked = true

    

}
/*******************validacion inputs carrousel*********/

/* Tallas */



let slideIndexT = 1;
function currentSlideT(m){
    tallas(slideIndexT = m)
}
let tallas = function(m){
    let tallaRadio = document.querySelectorAll(".radioTalla");
    let tallas = document.querySelectorAll(".tallas__container--item") 


    if(m > tallas.length) slideIndexT = 1
    if(m < 1) slideIndexT = tallas.length
    for(let i=0; i<tallas.length ;i++){
        tallas[i].className = tallas[i].className.replace("tallaActive","");
        

    }
    for(let i = 0; i < tallaRadio.length;i++){
        tallaRadio[i].checked = tallaRadio[i].checked=false
    }

    tallas[slideIndexT-1].className += " tallaActive";
    tallaRadio[slideIndexT-1].checked = true
} 





/* Colores */

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

/* Solo un color, selecciona el primero por defecto  */


let formularioDetalles = document.getElementById("formualioDetalles");
    formularioDetalles.addEventListener("submit",(e)=>{

    let tallaRadio = document.querySelectorAll(".radioTalla");
    if (tallaRadio[0].value == "Talla Unica") {
        tallaRadio[0].checked = true
        console.log(tallaRadio[0].value)}
    
    
    let colores = document.querySelectorAll('input[name="color"]')
    if(colores.length == 1 ){
        colores[0].checked = true
    }
    if(!document.querySelector('input[name="talla"]') == "" ){
        if(!document.querySelector('input[name="talla"]:checked')) {
            //alert('Error, selecciona una talla');
            window.alert('Error, selecciona una talla');
            e.preventDefault()
            }
        else{
            
        }
    }

    
})



