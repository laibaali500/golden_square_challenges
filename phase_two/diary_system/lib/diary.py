# File: lib/diary.py

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.readUpTo = 0 # the word in the contents the user has read up to

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return self.title + ": " + self.contents

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
        numberOfWords = wpm * minutes
        if (self.readUpTo + numberOfWords + 2) > self.count_words():
            self.readUpTo = 0
        chunk = self.contents.split()[self.readUpTo:(self.readUpTo + numberOfWords)]
        self.readUpTo += numberOfWords
        return " ".join(chunk)