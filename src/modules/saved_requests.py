import json


class SaveFileManager():
    def make_json_file(self, name, data):
            self.set_cwd()
            with open(f'save/{name}.json', 'w') as file:
                file.write(json.dumps(data))
        
    def load_json_file(self, name):
        self.set_cwd()
        with open(f'save/{name}.json', 'r') as file:
            raw = file.read() #reads contents
            return json.loads(raw) # converts json to proper python syntax

    def list_save_dir(self):
        self.set_cwd()
        return os.listdir("save/")