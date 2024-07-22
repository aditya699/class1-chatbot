import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response =  model.generate_content(f"{prompt}")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})