import streamlit as st
import asyncio
import websockets
import threading

st.title("Real-Time Chat App")

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

if 'ws' not in st.session_state:
    st.session_state.ws = None

def on_message(message):
    st.session_state.messages.append(f"User: {message}")
    st.experimental_rerun()

async def connect_to_websocket():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        st.session_state.ws = websocket
        while True:
            message = await websocket.recv()
            on_message(message)

def start_websocket_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(connect_to_websocket())

if st.session_state.ws is None:
    threading.Thread(target=start_websocket_thread, daemon=True).start()

for message in st.session_state.messages:
    st.write(message)

def send_message():
    if st.session_state.user_input and st.session_state.ws:
        asyncio.run(st.session_state.ws.send(st.session_state.user_input))
        st.session_state.user_input = ""

st.text_input("Type a message:", key="user_input")
st.button("Send", on_click=send_message)
