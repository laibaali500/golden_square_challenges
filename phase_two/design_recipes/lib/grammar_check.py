# File: lib/grammar_check.py

# Solution:
def grammar_check(sentence: str):
    """Check if a sentence is grammatically correct.
    
    Parameters:
        sentence: str -- a sentence to be checked
    
    Returns:
        bool -- is the sentence correct or not?
    
    Side effects:
        None
    
    """

    sentence_enders = [".", "!", "?"]
    if sentence[0].isupper() and sentence[-1] in sentence_enders:
        return True
    else:
        return False