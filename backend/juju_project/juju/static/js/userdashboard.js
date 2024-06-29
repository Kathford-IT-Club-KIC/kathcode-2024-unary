// userdashboard.js
let cart = [];

function addToCart(itemName, itemPrice, itemImage) {
    let item = {
        name: itemName,
        price: itemPrice,
        image: itemImage
    };
    cart.push(item);
    updateCartCount();
}

function updateCartCount() {
    let cartCount = document.getElementById('cart-count');
    cartCount.textContent = cart.length;
}
