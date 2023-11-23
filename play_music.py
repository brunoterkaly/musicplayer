from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def read_mp3_list_from_file(file_path):
    with open(file_path, 'r') as file:
        files = [line.strip().strip('"') for line in file.read().splitlines()]
        return [(f, os.path.basename(f)) for f in files]

@app.route('/')
def index():
    song_list = read_mp3_list_from_file("music_list.txt")
    return render_template('index.html', files=song_list)

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    selected_songs = request.json
    # Add logic to handle playlist creation
    print("Selected songs for playlist:", selected_songs)
    return jsonify({'message': 'Playlist created successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
