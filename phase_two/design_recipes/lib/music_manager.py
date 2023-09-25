# File: lib/music_manager

class MusicManager():

    def __init__(self):
        self.tracks = [] # a list of tuples

    def add_track(self, song: str, artist: str):
        # Parameters:
        #   song: the name of the song
        #   artist: the name of the artist
        if ((artist, song)) not in self.tracks:
            self.tracks.append((artist, song))

    def view_tracks(self):
        # Returns:
        #   str -- a formatted view of all tracks
        if len(self.tracks) > 0:
            tracks = []
            for i in self.tracks:
                tracks.append(f"{i[1]} by {i[0]}")
            return "\n".join(tracks)
        else:
            return "- No tracks added -"