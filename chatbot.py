import streamlit as st
import google.generativeai as genai
API_KEY="AIzaSyDY52-mLxf4s6mbHcGOyeYlVQN8FFb06Mw"

genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])

st.title("CHAT BOT - YOUR NIHGTMARE")
st.write("🤖🤖this is a chat bot made by Sindhu.... ")
if "messages" not in st.session_state:
  st.session_state.messages=[]

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input(" 😊What is up?"):
  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response=st.session_state.chat.send_message(prompt)

  st.session_state.messages.append({"role":"assistant","content":response.text})
  with st.chat_message("assistant"):
    st.markdown(response.text)
