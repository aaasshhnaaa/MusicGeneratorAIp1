import streamlit as st
import os
import gdown

MODEL_FILE = "music_generation_model.h5"

if not os.path.exists(MODEL_FILE):
    file_id = "1gaC0Y44Sr52XBq3q-rijiN5oOMqjmQWV"
    url = f"https://drive.google.com/uc?id={file_id}"

    gdown.download(url, MODEL_FILE, quiet=False)

    gdown.download(url, MODEL_FILE, quiet=False)

st.set_page_config(page_title="AI Music Generator", page_icon="🎵")

st.title("🎵 AI Music Generation using LSTM")
st.write("This project generates music using a Deep Learning (LSTM) model trained on MIDI files.")

st.subheader("Project Information")

st.markdown("""
- ✅ Deep Learning Model: LSTM
- ✅ Dataset: MIDI Music Files
- ✅ Framework: TensorFlow / Keras
- ✅ Library: Music21
""")

st.subheader("Generated Music")

if os.path.exists("generated_music.mid"):
    st.success("Music generated successfully!")

    with open("generated_music.mid", "rb") as file:
        st.download_button(
            label="🎼 Download Generated Music",
            data=file,
            file_name="generated_music.mid",
            mime="audio/midi"
        )

else:
    st.error("generated_music.mid not found.")

st.subheader("Model Information")

if os.path.exists("music_generation_model.h5"):
    st.success("Trained Model Loaded Successfully")
else:
    st.warning("Model file not found.")
