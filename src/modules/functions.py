import sys
import string

class Functions:

    def check_exit(self, check: str):
        if check == "exit":
            sys.exit(0)
        else:
            return
    
    def cap_input(self, words: str):
        words.replace("-", " ")
        string.capwords(words)
        words.replace(" ", "-")
        return words
