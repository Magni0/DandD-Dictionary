import os
import sys
import string

class Functions:

    def set_cwd(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
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
