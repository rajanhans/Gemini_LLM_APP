from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
api_key =""

with st.sidebar:
    api_key=st.text_input("Please provide your Gemini Pro API Key")
    genai.configure(api_key=api_key)
    "[Get a Gemini API key](https://makersuite.google.com/app/apikey)"
   


## function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_respone(question):
    response=chat.send_message(question, stream=True)
    return response

st.title("💬 Rajan's Chatbot-Google Gemini Pro")

st.text("!!! Please enter or create a Gemini Pro API key -see sidebar !!!")
st.divider()

#Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] 

input = st.text_input("Enter your question:", key="input")
submit=st.button("Ask your question")



if submit and input:
    if api_key =="" :
        st.error("Please enter Gemini Pro Key !")
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
