# File: lib/music_manager

class MusicManager():
    
    def __init__(self):
        self.tracks = {}

    def add_track(self, song: str, artist: str):
        # Parameters:
        #   song: the song by an artist
        #   artist: the artist of the song
        if ((artist, song)) not in self.tracks.items():
            self.tracks[artist] = song

    def view_tracks(self):
        # Returns:
        #   str -- a formatted view of artists and songs
        if len(self.tracks) > 0:
            tracks = []
            for i in self.tracks.items():
                tracks.append(f"{i[1]} by {i[0]}")
            return "\n".join(tracks)
        else:
            return "- No tracks added -"