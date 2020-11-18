import requests
import json


class ApiRequest:

    def specific_search(self, section, item):
        req = requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/{self.mutate_input(item)}/")
        return json.loads(req.text)

    def section_search(self, section):
        req = requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/")
        return json.loads(req.text)

    def section_list(self):
        req = requests.get(f"https://www.dnd5eapi.co/api/")
        return json.loads(req.text)

    # mutates str to fit api request
    def mutate_input(self, item):
        return item.lower().replace(" ", "-")
