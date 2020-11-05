import requests


class ApiRequest:

    def specific_search(self, section, item):
        return requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/{self.mutate_input(item)}/")

    def section_search(self, section):
        return requests.get(f"https://www.dnd5eapi.co/api/{self.mutate_input(section)}/")

    def section_list(self):
        return requests.get(f"https://www.dnd5eapi.co/api/")

    # mutates str to fit api request
    def mutate_input(self, item):
        return item.lower().replace(" ", "-")
