let cartList = document.getElementById("cartList");

function addToCart(id) {
    // if (localStorage.getItem("cart") === null) {
    //     localStorage.setItem("cart", JSON.stringify([]));
    // }
    // let cart = JSON.parse(localStorage.getItem("cart"));

    //TODO: use local storage to add items, or put the empty text automatically. 

    if (cartList.innerHTML === "") {
        cartList.innerHTML = "";
        pushCard(id);
    } else {
        pushCard(id);
    }
}

//FIXME: This is a placeholder function, it should be replaced with a real card and real information taken from the database.
function pushCard(id) {
    cartList.innerHTML += `
    <div class="cardContainer cardCart" id="card${id}">
        <img src="../assets/placeholder.png" alt="placeholder">
        <div class="cardContent">
            <div class="cardText">
                <h2>Burga la mas loca</h2>
                <p>Una burga de la reconcha de su hermana mal pero esta esta RE loca </p>
                <p class="gray">$200.000</p>
            </div>
            <button class="button" onclick="delFromCart(${id})">Borrar del carrito</button>
        </div>
    </div>`;
}

function delFromCart(id) {
    let card = document.getElementById(`card${id}`);
    card.remove();
}