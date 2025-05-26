import streamlit as st
import openai

# Ambil API key dari secrets
api_key = st.secrets["OPENROUTER_API_KEY"]
base_url = "https://openrouter.ai/api/v1"

# Inisialisasi client OpenAI
client = openai.OpenAI(api_key=api_key, base_url=base_url)

st.title("📄 Ringkasan Teks Otomatis")

text_input = st.text_area("Masukin teks panjang:", height=300)
prompt_input = st.text_input("Instruksi ringkasan (contoh: 'Ringkas jadi 3 kalimat')")

if st.button("Ringkas"):
    if not text_input or not prompt_input:
        st.warning("Isi teks dan instruksi dulu ya bro!")
    else:
        with st.spinner("Lagi ngeringkas..."):
            try:
                response = client.chat.completions.create(
                    model="openrouter/openai/gpt-3.5-turbo",  # pastikan ini model yang valid
                    messages=[
                        {"role": "system", "content": "Kamu asisten jago ngeringkas."},
                        {"role": "user", "content": f"{prompt_input}\n\n{text_input}"}
                    ]
                )
                hasil = response.choices[0].message.content
                st.success("✅ Sukses diringkas!")
                st.markdown("### ✨ Hasil Ringkasan:")
                st.write(hasil)
            except Exception as e:
                st.error(f"Gagal ngeringkas: {e}")
