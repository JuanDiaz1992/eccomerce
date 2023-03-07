
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

// Carrousel Productos

window.addEventListener("load", function(){
    let primerColorRadio = document.querySelector(".colorSection");
    primerColorRadio.checked = true;
    selectTalla(1);
  });

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n){
    showSlides(slideIndex += n)
}
function currentSlide(n){
    showSlides(slideIndex = n);
    selectTalla(slideIndex)
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
let selectTalla = function(o){
    let colorRadio = document.querySelectorAll(".colorSection");
    let tallaRadio = document.querySelectorAll(".radioTalla");
    let pTalla = document.querySelectorAll(".tallas__container--item")
    let colorSeleccionado = "";
    for(i = 0; i < colorRadio.length; i++){
        if(colorRadio[i].checked){
            colorSeleccionado = colorRadio[i].value;
            break;
        }
    }
    for(i = 0; i < tallaRadio.length; i++){
        if(tallaRadio[i].id === colorSeleccionado || tallaRadio[i].id === ""){
            pTalla[i].classList.add("visible")
            pTalla[i].classList.remove("oculto")
        } else {
            pTalla[i].classList.add("oculto")
            pTalla[i].classList.remove("visible")
        }
    }
    
}

/*******************validacion inputs carrousel*********/

/* Tallas */



let tallasContainer = document.querySelector('.tallas__container');
tallasContainer.addEventListener('click', function(event) {
    let clickedElement = event.target;
    if (clickedElement.classList.contains('tallas__container--item')) {
        let slideIndexT = 1;
        let tallaRadio = document.querySelectorAll(".radioTalla");
        let tallas = document.querySelectorAll(".tallas__container--item");

        for (let i = 0; i < tallas.length; i++) {
            tallas[i].classList.remove("tallaActive");
        }
        for (let i = 0; i < tallaRadio.length; i++) {
            tallaRadio[i].checked = false;
        }

        clickedElement.classList.add("tallaActive");
        let index = Array.from(tallas).indexOf(clickedElement);
        
        tallaRadio[index].checked = true;
        let tallaSeleccionada = document.querySelector('.radioTalla:checked');
        let stockP = document.querySelector('#stockP');
        if (stockP) {
            if (tallaSeleccionada) {
              let stock = tallaSeleccionada.getAttribute('data-stock');
              stockP.textContent =stock + ' disponibles';
            } else {
              stockP.textContent = '';
            }
          }

        
    }
});


/**********Función para ocultar Talla Unica */
(function() {
    let firstP = document.querySelector('.tallaUnica:first-of-type');
    let tituloTallas = document.getElementById("tituloTallas")
    if (firstP) {
      firstP.textContent = '';
      tituloTallas.textContent = ""
    }
  })();
  




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





/*Ajax para selección de producto en detalle */

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

let botonCaracteristicas = document.getElementById('buttonCaracteristicas')
botonCaracteristicas.addEventListener("click", function(event) {
    event.preventDefault();

    /*Si el elemento no incluye talla se envía como Talla Unica*/
    let tallaRadio = document.querySelectorAll(".radioTalla");
    if (tallaRadio[0].value == "Talla Unica") {
        tallaRadio[0].checked = true
        }
    
    /*Si el elemento incluye solo un color y contiene varias imagenes, siempre se selecciona la primer imagen*/
    let colores = document.querySelectorAll('input[name="color"]')
    if(colores.length == 1 ){
        colores[0].checked = true
    }
    /*Se previene que se envíe el formulario si no ha seleccionado una talla*/
    if(!document.querySelector('input[name="talla"]') == "" ){
        if(!document.querySelector('input[name="talla"]:checked')) {
            //alert('Error, selecciona una talla');
            window.alert('Error, selecciona una talla');
            e.preventDefault()
            }
        else{
            
        }
    }
    
    enviarAlCarro();

});



function enviarAlCarro(callback) {

    let form = new FormData(document.getElementById('formualioDetalles'));
    let url = `/agregarDetalle/`;
    fetch(url, {
        method: 'POST',
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(
        function(response){
            return response.json()
        }
    ).then(
        function(data){
            let cartNav = document.getElementById("totalCarro") 
            cartNav.textContent = JSON.stringify(data.data);
            let producto = JSON.stringify(data.producto);
            let tallaF = data.talla;
            let colorF = JSON.stringify(data.color);
            let talla = (tallaF === "Talla Unica") ? "" : `Talla: ${tallaF}`;
            let color = (colorF === "No incluye colores") ? "" : `Color: ${colorF}`;
            let mensaje = data.mensaje
            if (mensaje) {
                Swal.fire({
                    title: "Agregaste correctamente al carrito: ",
                    text: `${producto} ${talla}, ${color}`.replace(/"/g, "'").replace(/'/g, '') ,
                    icon: 'success', // o 'error', 'warning', 'info', etc.
                    confirmButtonText: 'Aceptar'
                })
            }else{
                Swal.fire({
                    title: "Ya excediste la cantidad disponible de este producto.",
                    text: `${producto} ${talla}, ${color}`.replace(/"/g, "'").replace(/'/g, '') ,
                    icon: 'error',
                    confirmButtonText: 'Aceptar'
                })
            }

            
        }
    )

    

}






