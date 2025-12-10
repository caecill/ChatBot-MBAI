import os, json
from langchain_google_genai import GoogleGenerativeAI

from intents import detect_intent
from sentiment import analyze_sentiment
from deteksi_resiko import detect_risk


# API KEY
GOOGLE_API_KEY = "AIzaSyCgq1GVZuS51v7xzILQpSZ0aiYpPYjjiRA"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Load model (versi baru)
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=GOOGLE_API_KEY,
    temperature=0.6,
    top_p=0.9
)


HISTORY_FILE = "chat_history.json"


def save_chat(role, text):
    chat = {"role": role, "text": text}

    # Jika file belum ada → buat baru
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([chat], f, indent=4)
        return

    # Jika file ada → append
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)

    data.append(chat)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


system_prompt = """
Kamu adalah SahabatBaikAI, chatbot anti-bullying yang sangat empatik.
Fokus: dukungan emosional, ketenangan, dan langkah aman.
"""


# ============ MODE TERMINAL (CLI) ============= #
print("\n=== SahabatBaikAI – Anti Bullying Advanced ===")
print("Ketik 'exit' untuk keluar.\n")

while True:
    user = input("Anda : ")

    if user.lower() == "exit":
        print("Chatbot: Terima kasih sudah curhat. Kamu berharga.")
        break

    save_chat("user", user)

    # Analitik tambahan
    intent = detect_intent(user)
    sentiment = analyze_sentiment(user)
    risk = detect_risk(user)

    analysis_text = f"""
Intent: {intent}
Sentimen: {sentiment}
Risiko: {risk}
"""

    # Panggil LLM (versi terbaru langsung string)
    full_prompt = (
        system_prompt
        + "\nPengguna: "
        + user
        + "\n\n"
        + analysis_text
        + "\nChatbot:"
    )

    answer = llm.invoke(full_prompt)

    save_chat("chatbot", answer)

    print("\nChatbot:", answer, "\n")
