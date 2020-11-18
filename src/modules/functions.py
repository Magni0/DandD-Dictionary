import os

class Functions:

    def set_cwd(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
