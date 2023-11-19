from flask import Flask, render_template, request, redirect, url_for
import subprocess
from urllib.parse import unquote
import re

app = Flask(__name__)

def is_safe_path(filename):
    # Basic check to ensure the filename doesn't contain malicious patterns
    # This should be enhanced for more security
    return not re.search(r'(\.\.\/|\.\.\\)', filename)

@app.route('/')
def index():
    file_list = read_mp3_list_from_file("music_list.txt")
    return render_template('index.html', files=file_list)

def read_mp3_list_from_file(file_path):
    with open(file_path, 'r') as file:
        # Strip whitespace and double quotes from each line (filename)
        return [line.strip().strip('"') for line in file.read().splitlines()]

@app.route('/play/<path:filename>')
def play(filename):
    # Decode URL-encoded filename
    filename = unquote(filename)
    print(f"Filename received: {filename}")  # Debug print

    # Remove double quotes from the filename
    filename = "/" + filename.strip('"')

    if not is_safe_path(filename):
        return "Invalid file path", 400

    # Construct the command
    command = f"open '{filename}'"
    subprocess.run(command, shell=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
