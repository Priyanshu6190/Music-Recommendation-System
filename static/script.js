function toTitleCase(str) {
    return str.toLowerCase().replace(/\b\w/g, char => char.toUpperCase());
}

function searchSong() {
    let query = document.getElementById("searchQuery").value.trim();
    let audioPlayer = document.getElementById("audioPlayer");
    let recommendationsList = document.getElementById("recommendations");
    let currentSong = document.getElementById("currentSong");
    let diskVideo = document.getElementById("diskVideo");

    if (query === "") {
        alert("Please enter a song name!");
        return;
    }

    fetch("http://127.0.0.1:5001/play", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ song_name: query })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert("❌ " + data.error);
            return;
        }

        audioPlayer.src = data.file;
        audioPlayer.play();
        diskVideo.play();

        currentSong.textContent = `Now Playing: ${toTitleCase(data.song_name)} - ${toTitleCase(data.artist)}`;

        recommendationsList.innerHTML = "";
        if (data.recommendations.length === 0) {
            recommendationsList.innerHTML = "<li>No recommendations available</li>";
        } else {
            data.recommendations.forEach((song, index) => {
                let li = document.createElement("li");
                li.textContent = `${index + 1}. ${toTitleCase(song.SongName)} - ${toTitleCase(song.ArtistName)}`;
                recommendationsList.appendChild(li);
            });
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while playing the song.");
    });
}

function playRecommended() {
    let indexInput = document.getElementById("songIndex").value.trim();
    let recommendations = document.getElementById("recommendations").children;

    if (indexInput === "") {
        alert("Please enter a song index.");
        return;
    }

    let index = parseInt(indexInput, 10);
    if (isNaN(index) || index < 1 || index > recommendations.length) {
        alert("Invalid index! Please enter a valid number.");
        return;
    }

    let songText = recommendations[index - 1].textContent;
    let songName = songText.split(" - ")[0].split(". ").slice(1).join(". ").trim();
    document.getElementById("searchQuery").value = songName;
    searchSong();
}

function seekSong(event) {
    const progressContainer = document.querySelector('.progress-bar-container');
    const progressBar = document.getElementById('progressBar');
    const audioPlayer = document.getElementById('audioPlayer');

    const rect = progressContainer.getBoundingClientRect();
    const clickX = event.clientX - rect.left;
    const width = rect.width;
    const seekTime = (clickX / width) * audioPlayer.duration;
    audioPlayer.currentTime = seekTime;
}

function updateProgressBar() {
    const audioPlayer = document.getElementById("audioPlayer");
    const progressBar = document.getElementById("progressBar");
    const percentage = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    progressBar.style.width = percentage + "%";
}

document.getElementById("audioPlayer").addEventListener("timeupdate", updateProgressBar);
