const API = "http://127.0.0.1:8000";

// Load Menu
async function loadMenu() {

    try {

        const response =
            await fetch(`${API}/menu`);

        const data =
            await response.json();

        const menuContainer =
            document.getElementById("menu-container");

        menuContainer.innerHTML = "";

        data.forEach(item => {

            menuContainer.innerHTML += `
                <div class="card">
                    <h3>${item.name}</h3>
                    <p>Price: ₹${item.price}</p>
                    <p>${item.category}</p>

                    <button onclick="addToCart(${item.id})">
                        Add To Cart
                    </button>
                </div>
            `;
        });

    } catch(error) {
        console.log(error);
        alert("Cannot connect to backend");
    }
}

// Add to Cart
async function addToCart(id){

    await fetch(
        `${API}/cart/add?item_id=${id}&quantity=1`,
        {
            method:"POST"
        }
    );

    loadCart();
}

// Load Cart
async function loadCart(){

    const response =
        await fetch(`${API}/cart`);

    const data =
        await response.json();

    const cartContainer =
        document.getElementById("cart-container");

    cartContainer.innerHTML = "";

    data.cart.forEach(item => {

        cartContainer.innerHTML += `
            <p>
                ${item.name}
                x ${item.qty}
                =
                ₹${item.qty * item.price}
            </p>
        `;
    });

    document.getElementById("total").innerHTML =
        `Total: ₹${data.total}`;
}

// Checkout
async function checkout(){

    const customer =
        document.getElementById("customer").value;

    const address =
        document.getElementById("address").value;

    if(customer === "" || address === ""){
        alert("Enter customer details");
        return;
    }

    const response =
        await fetch(
            `${API}/cart/checkout`,
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    customer_name: customer,
                    delivery_address: address
                })
            }
        );

    const result =
        await response.json();

    alert("Order Placed Successfully");

    console.log(result);

    loadCart();
}

// Initial Load
loadMenu();
loadCart();