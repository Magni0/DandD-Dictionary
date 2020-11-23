import requests
import json


class ApiRequest:

    def item_search(self, section: str, item: str):
        req = requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/{self.mutate_input(item)}/")
        return json.loads(req.text)

    def section_search(self, section: str):
        req = requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/")
        return json.loads(req.text)

    def list_sections(self):
        req = requests.get(f"https://www.dnd5eapi.co/api/")
        return json.loads(req.text)

    # mutates str to fit api request
    def mutate_input(self, item: str):
        return item.lower().replace(" ", "-")
