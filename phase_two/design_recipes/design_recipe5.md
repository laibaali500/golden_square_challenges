## Function Design Recipe 5

## 1. Describe the Problem

_User story 4:_

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

```python
class MusicManager():
    
    def __init__(self):
        pass

    def add_track(self, song: str, artist: str):
        # Parameters:
        #   song: the song by an artist
        #   artist: the artist of the song
        pass

    def view_tracks(self):
        # Returns:
        #   str -- a formatted view of artists and songs
        pass
```

## 3. Create Examples as Tests

_A list of examples of what the function will take and return._

```python
"""
Given a track to add
Viewing the tracks returns the track
"""
manager = MusicManager()
manager.add_track("Arabesque", "Lily Chou-Chou")
manager.view_tracks() => ("Arabesque by Lily Chou-Chou")

"""
Given two tracks to add
Viewing the tracks returns the tracks
"""
manager = MusicManager()
manager.add_track("Arabesque", "Lily Chou-Chou")
manager.add_track("Porcelain", "Ichiko Aoba")
manager.view_tracks() => ("Arabesque by Lily Chou-Chou\nPorcelain by Ichiko Aoba")

"""
Given no tracks to add
Viewing the tracks returns a message saying "No tracks added."
"""
manager = MusicManager()
manager.view_tracks() => ("- No tracks added -")

"""
Given the same tracks to add
Viewing the tracks returns just one of the tracks
"""
manager = MusicManager()
manager.add_track("Arabesque", "Lily Chou-Chou")
manager.add_track("Arabesque", "Lily Chou-Chou")
manager.view_tracks() => ("Arabesque by Lily Chou-Chou")
```