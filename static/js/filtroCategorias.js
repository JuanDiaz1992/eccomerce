/*Ajax para filtrar los elementos de las categorías */
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



let filtrarProductos = (event)=> {
    event.preventDefault();
    
    let urlFiltro = `/filtrarCategoria/`;
    let formFiltro = new FormData(document.getElementById("filtrarProducto")) 
    fetch(urlFiltro, {
        method: 'POST',
        body: formFiltro,
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
        let marca = data.marca;
        let genero = data.genero;
        let productos = data.productos;
        const listado = document.querySelector('.listado');
        listado.innerHTML = '';
          // Iterar por cada producto y agregarlo al HTML
        productos.forEach(producto => {
            const htmlProducto = `
            <div class="card">
                <a href="{% url 'tiendaEnLinea:detail' ${producto.id} %}">
                <picture class="card__picture--container">
                    <img class="categoria__imagen" src="${producto.imagen}" alt="imagen">
                </picture>
                <div class="categoria__text">
                    <h5 class="bg-3 marca">Por ${producto.marca}</h5>
                    <p class="bg-2">${producto.nombre}</p>
                    <p class="precio">${producto.descuento == 0 ? `
                    <h5 class="bg-2">$${producto.precio.toLocaleString()} </h5>
                    <p class="sinDescuento"></p>
                    <div>
                    <h5 class="bg-2"></h5> 
                    <p class="descuento"></p>
                </div>    
                ` : `
                <p class="sinDescuento">$${producto.precioSinDescuento.toLocaleString()}</p>
                <div class="descuento__detalle">
                    <h5 class="bg-2">$${producto.precio.toLocaleString()} </h5> 
                    <p class="descuento">${producto.descuento}% OFF</p>
                </div>
                `}
                </div>
                </div>
                </a>
            </div>
            `;
            listado.insertAdjacentHTML('beforeend', htmlProducto);
        });


        }
    )



}

let botonFiltroCategoria = document.getElementById('botonFiltro')
botonFiltroCategoria.addEventListener("click",filtrarProductos);


