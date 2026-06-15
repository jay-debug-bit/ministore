import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# -------------------------
# Product Database
# -------------------------

products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "category": "Electronics",
        "description": "Premium noise-cancelling headphones."
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "category": "Electronics",
        "description": "Track fitness and notifications."
    },
    {
        "name": "Gaming Mouse",
        "price": 1499,
        "category": "Accessories",
        "description": "RGB ergonomic gaming mouse."
    },
    {
        "name": "Mechanical Keyboard",
        "price": 3999,
        "category": "Accessories",
        "description": "Mechanical keyboard with RGB lighting."
    },
    {
        "name": "Laptop Backpack",
        "price": 1999,
        "category": "Bags",
        "description": "Water-resistant backpack for travel."
    },
    {
        "name": "Bluetooth Speaker",
        "price": 2499,
        "category": "Electronics",
        "description": "Portable speaker with powerful bass."
    }
]

# -------------------------
# Session State
# -------------------------

if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#1f77b4;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    color:black;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
    margin-bottom:10px;
}

.cart-box{
    background:#f0f2f6;
    padding:10px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown(
    "<div class='main-title'>🛒 MiniStore</div>",
    unsafe_allow_html=True
)

st.write("## Welcome to MiniStore")
st.write(
    "Discover premium electronics and accessories at affordable prices."
)

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Categories")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

st.sidebar.markdown("---")

st.sidebar.title("Cart Summary")

total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.markdown(
    f"""
    <div class='cart-box'>
    <b>Items:</b> {len(st.session_state.cart)}<br>
    <b>Total:</b> ₹{total}
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Filter Products
# -------------------------

filtered_products = products

if selected_category != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# -------------------------
# Product Display
# -------------------------

st.subheader("Featured Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(
            f"""
            <div class="product-card">
            <h3>{product['name']}</h3>
            <p>{product['description']}</p>
            <h4>₹{product['price']}</h4>
            <b>Category:</b> {product['category']}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(
                f"{product['name']} added to cart!"
            )

# -------------------------
# Support Navigation
# -------------------------

st.markdown("---")

if st.button("💬 Open Customer Support"):
    st.switch_page("pages/1_Support_Chatbot.py")