# ChatBot Anti-Bully  
Sistem chatbot sederhana berbasis **Streamlit** dan **OpenAI API** yang bertujuan membantu pengguna menghadapi kasus bullying dengan memberikan respons edukatif dan suportif.

---

### Fitur
- Chatbot interaktif berbasis **OpenAI GPT**.
- Antarmuka web menggunakan **Streamlit**.
- Respons ramah dan aman dengan fokus anti-bullying.
- Penyimpanan riwayat percakapan selama sesi berjalan.
- Mudah dijalankan secara lokal.

---
### Persyaratan Sistem
Pastikan sudah menginstall:
- Python 3.9 atau versi lebih baru
- pip (package manager)

---

### Instalasi
1. Clone Repositori
  ```bash
    git clone https://github.com/caecill/ChatBot-MBAI.git
    cd ChatBot
  ```

2. (Opsional tapi disarankan) Buat Virtual Environment
  ```bash
   conda create -n chatbot-project python=3.10
   conda activate chatbot-project
  ```
3. Install Dependencies
 ```bash
   pip isntall -r requirements.txt
 ```

---

### Konfigurasi API Key
Edit file chatbot.py dan masukkan Google API Key Kamu pada baris code dibawah:
  ```bash
  os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
  ```
Kamu bisa mendapatkannya dari:
https://aistudio.google.com/

---

### Menjalankan Aplikasi
```bash
  python -m streamlit run ui.py
 ```
