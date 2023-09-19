def make_snippet(string):
    wordList = string.split()
    snippet = ' '.join(wordList[:5])
    if len(wordList) > 5:
        snippet += " ..."
    return snippet


def count_words(string):
    return len(string.split())
