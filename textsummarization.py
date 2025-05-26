import streamlit as st
import openai

# Atur API key dan base URL OpenRouter
openai.api_key = "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"  # pastiin diawali openrouter-
openai.base_url = "https://openrouter.ai/api/v1"

# Inisialisasi client
client = openai.OpenAI(api_key=openai.api_key, base_url=openai.base_url)

# UI
st.set_page_config(page_title="Ringkas Teks via OpenRouter", layout="centered")
st.title("📝 Ringkasan Teks Otomatis")

text_input = st.text_area("Masukin teks panjang yang mau diringkas:", height=300)
custom_prompt = st.text_input("Instruksi ringkasan (misal: 'Ringkas dalam 3 kalimat, tetap pakai bahasa aslinya'):")

if st.button("🔍 Ringkas"):
    if text_input.strip() == "" or custom_prompt.strip() == "":
        st.warning("Tolong isi kedua kolom dulu ya!")
    else:
        with st.spinner("Lagi ngeringkas teks lu, bentar ya..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Kamu adalah asisten yang jago meringkas teks panjang."},
                        {"role": "user", "content": f"{custom_prompt}\n\n{text_input}"}
                    ]
                )
                hasil = response.choices[0].message.content
                st.success("Berhasil diringkas!")
                st.markdown("### ✨ Hasil Ringkasan:")
                st.write(hasil)
            except Exception as e:
                st.error(f"Gagal ngeringkas: {e}")
