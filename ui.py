import streamlit as st
from chatbot import llm, system_prompt, save_chat
from intents import detect_intent
from sentiment import analyze_sentiment
from deteksi_resiko import detect_risk

st.write("DEBUG: UI LOADED")

st.title("🌈 SahabatBaikAI – Anti Bullying Chatbot")

user_input = st.text_input("Ketik pesan Anda:")

send_button = st.button("Kirim")

if send_button and user_input:
    save_chat("user", user_input)

    intent = detect_intent(user_input)
    sentiment = analyze_sentiment(user_input)
    risk = detect_risk(user_input)

    analysis_text = f"""
    Intent: {intent}
    Sentimen: {sentiment}
    Risiko: {risk}
    """

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input + "\n\n" + analysis_text}
    ])

    answer = response.content

    save_chat("chatbot", answer)

    st.write("### Chatbot:")
    st.write(answer)
