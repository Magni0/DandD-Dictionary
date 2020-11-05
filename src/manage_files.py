import json

class FileManagement:

    def load_json(self, response):
        return json.loads(response.text)
    
    def save_file(self, name, data):
        with open(f'{name}.txt', 'w') as file:
            file.write(data)
