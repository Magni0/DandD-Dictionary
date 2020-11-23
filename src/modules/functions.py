import sys
import string

class Functions:

    def if_value(self, check):
        try:
            return check
        except:
            return "None"

    def check_exit(self, check):
        if check == "exit":
            sys.exit(0)
        else:
            return
    
    def cap_input(self, words: str):
        words.replace("-", " ")
        string.capwords(words)
        words.replace(" ", "-")
        return words
