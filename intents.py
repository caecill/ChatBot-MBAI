def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["diejek", "dibully", "dihina", "dikatain"]):
        return "lapor_bullying"

    if any(word in text for word in ["sedih", "capek", "lelah", "kesepian", "marah"]):
        return "curhat"

    if "apa itu bullying" in text or "jenis bullying" in text:
        return "tanya_informasi"

    if any(word in text for word in ["saran", "harus gimana", "aku harus apa"]):
        return "minta_saran"

    return "lainnya"
