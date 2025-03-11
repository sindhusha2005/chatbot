import streamlit as st
import google.generativeai as genai
API_KEY =AIzaSyDY52-mLxf4s6mbHcGOyeYlVQN8FFb06Mw
genai.configure
model=genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])
st.title(" chatbot - Your nightmare")
st.write( "🤖 This is a chatbot made by Sindhu...")
if "messages" not in st.session_state:
  st.session_state.messages=[]
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt:=st.chat_input("Say something"):
  st.session_state.messages.append({"role":"user","content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response=st.session_state.chat.send_message(prompt)
  st.session_state.messages.append({"role":"assistant","content":response.text})
  with st.chat_message("assistant"):
    st.markdown(response.text)
  
