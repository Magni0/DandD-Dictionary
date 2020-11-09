import json
import os

class Functions:

    def set_cwd(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # def make_txt_file(self, name, data):
    #     self.setcwd()
    #     with open(f'{name}.txt', 'w') as file:
    #         file.write(data)

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
    
    def pretty_list(self, data):
        list_data = data.keys()
        for item in list_data:
            print(item)
        return list_data