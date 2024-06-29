// cart.js
let cart = []; // This will hold the items added from index.html

function displayCartItems() {
    let cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = '';

    cart.forEach(item => {
        let cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');

        // Create image element
        let imgElement = document.createElement('img');
        imgElement.src = item.image;
        imgElement.alt = item.name;
        cartItem.appendChild(imgElement);

        // Create name element
        let nameElement = document.createElement('div');
        nameElement.textContent = item.name;
        cartItem.appendChild(nameElement);

        // Create price element
        let priceElement = document.createElement('div');
        priceElement.textContent = `Rs ${item.price}`;
        cartItem.appendChild(priceElement);

        cartItemsContainer.appendChild(cartItem);
    });
}

function checkout() {
    // Implement checkout logic (redirect to payment page or similar)
    alert('Redirecting to checkout...');
    // Add your checkout logic here
}

// Function to initialize cart display when the page loads
window.onload = function() {
    displayCartItems();
};
