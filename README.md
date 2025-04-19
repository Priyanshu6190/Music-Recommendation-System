🎧 Music Mood Recommendation System

This project is a Music Recommendation System that classifies songs into different moods using machine learning and recommends similar songs based on mood. It includes a beautiful web UI, a custom audio player, and YouTube song streaming integration using Flask and JavaScript.

---

🚀 Features

- 🎶 Classifies songs into 20+ moods using audio features
- 🧠 Uses a trained Random Forest Classifier for mood prediction
- 🔎 Song search and playback with YouTube integration
- 💽 Spinning disk animation and custom audio player
- 🎵 Dynamic mood-based song recommendations
- 🔁 Option to play recommended songs by selecting an index

---

🛠️ Tech Stack

| Frontend  :  HTML, CSS, JavaScript |
| Backend   :  Flask, Python    |

---

🧪 How It Works

1. Preprocessing:
   - Read `SpotifySongs.csv` dataset.
   - Clean and select relevant audio features.
   - Encode mood labels.

2. Web Interface:
   - User searches for a song name.
   - Flask fetches the YouTube audio, classifies the mood, and plays it.
   - Recommendations of songs with similar moods are displayed.

---

📊 Dataset
Uses SpotifySongs.csv which contains audio features like Energy, Valence, Danceability, etc.

Each song is labeled with a mood either via rules or ML prediction.

📌 TODOs / Future Improvements
 Add genre-based filtering

 Improve accuracy using deep learning models

 Deploy using Docker or Streamlit Cloud

 Add user login & playlists

📃 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
Audio features provided by Spotify API

Model training powered by Scikit-learn

Video/audio integration inspired by Spotify UI

📬 Contact
Mail me : priyanshu619rana@gmail.com
