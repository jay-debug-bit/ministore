import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Customer Support")

# -------------------------
# Product Knowledge
# -------------------------

products = [
    "Wireless Headphones",
    "Smart Watch",
    "Gaming Mouse",
    "Mechanical Keyboard",
    "Laptop Backpack",
    "Bluetooth Speaker"
]

# -------------------------
# Chat History
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Rule-Based Bot
# -------------------------

def get_response(user_text):

    text = user_text.lower()

    # Products
    for product in products:
        if product.lower() in text:
            return (
                f"{product} is available in our store."
            )

    # Delivery

    if "delivery" in text or "shipping" in text:
        return (
            "Orders are typically delivered within 3-7 business days."
        )

    # Refund

    if "refund" in text:
        return (
            "Refunds are processed within 5-7 business days after approval."
        )

    # Return

    if "return" in text:
        return (
            "Products can be returned within 7 days of delivery."
        )

    # Payment

    if "payment" in text or "upi" in text:
        return (
            "We accept UPI, Credit Card, Debit Card and Net Banking."
        )

    # Order

    if "order" in text or "status" in text:
        return (
            "Please provide your order ID to check order status."
        )

    return (
        "I can help with products, delivery, refunds, returns, payments and order status."
    )

# -------------------------
# Chat Input
# -------------------------

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# -------------------------
# Back Button
# -------------------------

st.markdown("---")

if st.button("⬅ Back to Store"):
    st.switch_page("app.py")