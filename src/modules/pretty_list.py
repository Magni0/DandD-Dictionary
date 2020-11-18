
class PrettyList():
    def pretty_list_sections(self, data):
        list_data = data.keys()
        for item in list_data:
            print(item)
        return list_data

    def pretty_section_search(self, data):
        list_data = []
        print(f"Total count: {data['count']}")
        for name in data["results"]:
            print(name["name"])
            list_data.append(name["name"])
        return list_data

    def pretty_specific_search(self, data):
        pass
