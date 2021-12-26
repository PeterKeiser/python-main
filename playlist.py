# playlist

playlist = {
    "title": "patagonia bus", 
    "author": "Colt", 
    "songs": [
        {"title": "song1", "artist": ["blue"], "duration": 2.5 },
        {"title": "song2", "artist": ["kitty", "djcat"], "duration": 5.25 },
        {"title": "meowmeow", "artist": ["garfield"], "duration": 2.0 },
    ] 
}

print(playlist)

total_length = 0
for song in playlist ["songs"]:
    total_length += song["duration"]
    print(song["duration"])
    print(total_length)
    
