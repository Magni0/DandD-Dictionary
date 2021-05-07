import json
import os

class SaveFileManager():
    def set_cwd(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    def make_json_file(self, name: str, data: dict):
        self.set_cwd()
        with open(f'save/{name}.json', 'w') as file:
            file.write(json.dumps(data))

    def load_json_file(self, name: str):
        self.set_cwd()
        with open(f'save/{name}.json', 'r') as file:
            raw = file.read() #reads contents
            return json.loads(raw) # converts json to proper python syntax

    def list_save_dir(self):
        self.set_cwd()
        return os.listdir("save/")
