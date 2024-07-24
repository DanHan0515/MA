import streamlit as st

# Initialize the session state for messages and user input if not already done
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

def send_message():
    if st.session_state.user_input:
        st.session_state.messages.append(f"User: {st.session_state.user_input}")
        st.session_state.user_input = ""

st.title("Streamlit Chat App")

# Display chat messages
for message in st.session_state.messages:
    st.write(message)

# User input for new message
st.text_input("Type a message:", key="user_input", on_change=send_message)

# Button to send message
st.button("Send", on_click=send_message)

# Refresh chat messages every few seconds
st.write("Refreshing messages...")
