from flask import Flask, render_template, request, jsonify
import os
import subprocess
import sys

# Flask app configuration
app = Flask(__name__)
MUSIC_LIST_FILE = "music_list.txt"
PLAYLIST_FILE = "yacht_playlist.m3u"

def read_mp3_list_from_file(file_path):
    """Read MP3 file paths from a file and return a list of tuples with file path and basename."""
    try:
        with open(file_path, 'r') as file:
            files = [line.strip().strip('"') for line in file.read().splitlines()]
            return [(f, os.path.basename(f)) for f in files]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []


def write_playlist(playlist_tracks, file_path):
    """Write the list of tracks to a playlist file."""
    try:
        with open(file_path, "w") as playlist_file:
            for track in playlist_tracks:
                playlist_file.write(track + "\n")
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")

def open_file(file_path):
    """Open a file using the default application based on the operating system."""
    if sys.platform == "win32":
        os.startfile(file_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", file_path])
    elif sys.platform.startswith("linux"):
        subprocess.run(["xdg-open", file_path])
    else:
        print("Unsupported OS")

@app.route('/')
def index():
    """Render the main page with a list of songs."""
    song_list = read_mp3_list_from_file(MUSIC_LIST_FILE)
    return render_template('index.html', files=song_list)

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    """Create a playlist from selected songs."""
    selected_songs = request.json
    write_playlist(selected_songs, PLAYLIST_FILE)
    open_file(PLAYLIST_FILE)
    print("Selected songs for playlist:", selected_songs)
    return jsonify({'message': 'Playlist created successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
