# File: lib/grammar_stats.py

class GrammarStats:
    def __init__(self):
        self.record = []
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        punctuation = ["!", ".", "?"]
        result = text[0].isupper() and (text[-1] in punctuation)
        self.record.append(result)
        return result
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        numOfPassed = self.record.count(True)
        return (numOfPassed/len(self.record)) * 100