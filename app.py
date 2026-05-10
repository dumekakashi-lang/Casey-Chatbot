import streamlit as st
from nltk.chat.util import Chat, reflections

pairs = [
    ["halo", ["Halo juga!", "Hai!"]],
    ["nama kamu siapa?", ["Saya chatbot buatan kamu"]],
    ["apa kabar?", ["Saya baik!", "Kamu gimana?"]],
    ["bye", ["Sampai jumpa!"]]
]

chatbot = Chat(pairs, reflections)

st.title("Chatbot AI Sederhana")

user_input = st.text_input("Kamu:")

if user_input:
    response = chatbot.respond(user_input)
    st.write("AI:", response)
