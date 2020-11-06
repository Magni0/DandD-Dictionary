import json

class Functions:

    def make_txt_file(self, name, data):
        with open(f'{name}.txt', 'w') as file:
            file.write(data)

    def make_json_file(self, name, data):
        with open(f'{name}.json', 'w') as file:
            file.write(json.dumps(data))
    
    def load_json_file(self, name):
        with open(f'{name}.json', 'r') as file:
            raw = file.read() #reads contents
            return json.loads(raw) # converts json to proper python syntax
    
    def dict_to_list_of_keys(self, data):
        data_list = []
        [key for key in data.keys()]
        return data_list