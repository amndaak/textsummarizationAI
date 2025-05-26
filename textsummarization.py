import streamlit as st
import openai

# Ambil API key dari secrets
api_key = st.secrets["OPENROUTER_API_KEY"]
base_url = "https://openrouter.ai/api/v1"

# Inisialisasi client
client = openai.OpenAI(api_key=api_key, base_url=base_url)

st.title("📄 Ringkasan Teks Otomatis")
st.markdown("Masukkan teks panjang yang mau diringkas, dan tentukan mau diringkas kayak gimana!")

text_input = st.text_area("Masukin teks yang mau diringkas:", height=300)
prompt_input = st.text_input("Instruksi ringkasan (contoh: 'Ringkas jadi 3 kalimat')")

if st.button("Ringkas"):
    if not text_input or not prompt_input:
        st.warning("Isi dulu dua-duanya bro!")
    else:
        with st.spinner("Lagi ngeringkas..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Kamu asisten jago ngeringkas."},
                        {"role": "user", "content": f"{prompt_input}\n\n{text_input}"}
                    ]
                )
                hasil = response.choices[0].message.content
                st.success("✅ Berhasil diringkas!")
                st.markdown("### ✨ Hasil Ringkasan:")
                st.write(hasil)
            except Exception as e:
                st.error(f"Gagal meringkas: {e}")
