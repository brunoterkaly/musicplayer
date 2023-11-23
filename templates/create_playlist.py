# List of songs for the playlist
playlist_tracks = [
    "/Users/brunoterkaly/yacht_mp3/OnAndOnoRrlRbGT.mp3",
    "/Users/brunoterkaly/yacht_mp3/IGoCrazyw.mp3",
    "/Users/brunoterkaly/yacht_mp3/Africaw.mp3"
]

# Create and write to the M3U file
with open("/Users/brunoterkaly/yacht_playlist.m3u", "w") as playlist_file:
    for track in playlist_tracks:
        playlist_file.write(track + "\n")
