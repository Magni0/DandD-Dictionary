
class PrettySearch():
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

    # def pretty_specific_search(self, data):
    #     pass

class PrettyItem():
    def pretty_ability_scores(self, data):
        pass

    def pretty_classes(self, data):
        pass

    def pretty_conditions(self, data):
        pass

    def pretty_damage_types(self, data):
        pass

    def pretty_equipment_categories(self, data):
        pass

    def pretty_equipment(self, data):
        pass

    def pretty_features(self, data):
        pass

    def pretty_languages(self, data):
        pass

    def pretty_magic_items(self, data):
        pass

    def pretty_magic_schools(self, data):
        pass

    def pretty_monsters(self, data):
        pass

    def pretty_proficiencies(self, data):
        pass

    def pretty_races(self, data):
        pass

    def pretty_rules(self, data):
        pass
    
    def pretty_rule_sections(self, data):
        pass

    def pretty_skills(self, data):
        pass

    def pretty_spells(self, data):
        pass

    def pretty_starting_equipment(self, data):
        pass

    def pretty_subclasses(self, data):
        pass

    def pretty_subraces(self, data):
        pass

    def pretty_traits(self, data):
        pass

    def pretty_weapon_properties(self, data):
        pass