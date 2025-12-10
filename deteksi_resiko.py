def detect_risk(text):
    text = text.lower()

    high_risk_words = [
        "bunuh diri", "mengakhiri hidup", "ga kuat", "ingin mati",
        "putus asa", "tak berharga"
    ]

    if any(word in text for word in high_risk_words):
        return "tinggi"

    if any(word in text for word in ["cemas", "stress", "takut", "khawatir"]):
        return "sedang"

    return "rendah"
