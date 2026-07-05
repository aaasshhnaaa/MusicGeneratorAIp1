# 🎵 Music Generation with AI

## 📌 Project Overview

This project uses Artificial Intelligence and Deep Learning (LSTM Neural Network) to generate new music from a collection of MIDI files.

The model learns musical note patterns from existing MIDI songs and generates a completely new MIDI composition.

---

## 🚀 Features

- Load multiple MIDI music files
- Extract notes and chords using Music21
- Preprocess music into note sequences
- Train an LSTM-based deep learning model
- Generate new music sequences
- Save generated music as a MIDI file

---

## 📂 Project Structure

MusicGeneratorAIp1/
│── MusicGenerator.ipynb
│── music_generation_model.h5
│── generated_music.mid
│── README.md
│── requirements.txt
│── midi_songs/
│ ├── song1.mid
│ ├── song2.mid
│ └── ...

---

## 🛠 Technologies Used

- Python
- TensorFlow / Keras
- Music21
- NumPy

---

## 📊 Workflow

1. Collect MIDI music files.
2. Extract notes and chords.
3. Create input-output sequences.
4. Train an LSTM model.
5. Generate new music.
6. Save the generated music as a MIDI file.

---

---

## 📁 Dataset

The project uses a collection of MIDI (.mid) files placed inside the `midi_songs` folder.

---

## 📌 Output

- Trained LSTM Model (`music_generation_model.h5`)
- Generated MIDI Music (`generated_music.mid`)

---

## 👩‍💻 Author

Aashna Mehta
