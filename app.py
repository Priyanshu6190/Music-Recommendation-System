from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import yt_dlp
import os
import random

app = Flask(__name__)
CORS(app)

# Google Sheet Configuration
SHEET_ID = "1qYXolZa5zJQtz58P64QGzYBnwE5hUiDVVO9LWN_1Blo"
SHEET_NAME = "Sheet1"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

COOKIES_PATH = "cookies.txt"
STATIC_DIR = "static"

os.makedirs(STATIC_DIR, exist_ok=True)

# Load Dataset
try:
    dataset = pd.read_csv(SHEET_URL)
    dataset = dataset.where(pd.notna(dataset), None)  # Replace NaN with None
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    dataset = pd.DataFrame()

if "SongName" in dataset.columns:
    dataset["SongName"] = dataset["SongName"].astype(str).str.strip().str.lower()
    print("✅ Available Songs:", dataset["SongName"].tolist())

def get_audio_url(url, song_name):
    safe_song_name = "".join(c if c.isalnum() or c in " -" else "" for c in song_name)
    filename = os.path.join(STATIC_DIR, f"{safe_song_name}.mp3")

    if os.path.exists(filename):
        return f"/static/{os.path.basename(filename)}"

    options = {
        'cookiefile': COOKIES_PATH,
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',
        'outtmpl': filename,
        'quiet': True,
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"❌ Error downloading song: {e}")
            return None

    return f"/static/{os.path.basename(filename)}" if os.path.exists(filename) else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play_song():
    try:
        data = request.json
        song_name = data.get("song_name", "").strip()
        if ". " in song_name:
            song_name = song_name.split(". ", 1)[1]
            
        song_name = song_name.lower()


        print(f"🔍 Searching for: {song_name}")

        if "SongName" not in dataset.columns or "Mood" not in dataset.columns:
            return jsonify({"error": "Dataset missing required columns"}), 500

        song_row = dataset[dataset["SongName"].str.lower() == song_name]

        if song_row.empty:
            return jsonify({"error": "Song not found"}), 404

        url = song_row.iloc[0].get("Song Link")
        artist = song_row.iloc[0].get("ArtistName", "Unknown Artist")
        mood = song_row.iloc[0].get("Mood", "").strip().lower()

        print(f"🎵 Mood detected: {mood}")

        dataset["Mood"] = dataset["Mood"].str.strip().str.lower()  # Normalize all moods
        mood = mood.strip().lower()  # Normalize input mood
        recommendations = dataset[dataset["Mood"] == mood]  # Now it should match correctly


        recommendations = recommendations.replace({np.nan: "Unknown"})  # Fix NaN issue
        recommended_songs = recommendations.sample(n=min(10, len(recommendations)), random_state=None).to_dict(orient="records")

        print(f"✅ Found {len(recommended_songs)} recommendations")

        return jsonify({
            "message": "Playing",
            "file": get_audio_url(url, song_name),
            "song_name": song_name,
            "artist": artist,
            "recommendations": recommended_songs
        })

    except Exception as e:
        print(f"❌ Error in /play: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
