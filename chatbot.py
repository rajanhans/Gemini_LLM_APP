from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

with st.sidebar:
    genai.configure(api_key=st.text_input("Please provide your Gemini Pro API Key"))
    "[Get a Gemini API key](https://makersuite.google.com/app/apikey)"
    "[View the source code](https://github.com/rajanhans/Gemini_LLM_APP/chatbot.py)"



## function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_respone(question):
    response=chat.send_message(question, stream=True)
    return response

st.title("💬 Rajan's Chatbot-Google Gemini Pro")

#Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] 

input = st.text_input("Input:", key="input")
submit=st.button("Ask the question")

if submit and input:
    response = get_gemini_respone(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
