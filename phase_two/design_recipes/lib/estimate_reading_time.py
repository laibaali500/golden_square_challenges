# File: lib/estimate_reading_time.py

#Solution:
def estimate_reading_time(words):
    """Calculate reading time, given text length and reading speed.
    
    Parameters:
        words: int -- number of words in the text
    
    Returns:
        int -- estimated reading time in minutes
    
    Side effects:
        None
    """

    SPEED = 200 # words per minute
    time = words / SPEED
    return time