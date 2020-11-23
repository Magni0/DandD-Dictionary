
class PrettySearch():
    def pretty_list_sections(self, data: dict):
        list_data = data.keys()
        for item in list_data:
            print(item)
        return list_data

    def pretty_section_search(self, data: dict):
        list_data = []
        print(f"Total count: {data['count']}")
        for name in data["results"]:
            print(name["name"])
            list_data.append(name["name"])
        return list_data

    # def pretty_specific_search(self, data):
    #     pass

class PrettyItem():
    def pretty_ability_scores(self, data: dict):
        list_ability_scores = []
        [list_ability_scores.append(score['name']) for score in data['results']]
        ability_scores = ", ".join(list_ability_scores)

        return [f"Results: {data['count']}", f"Ability Scores: {ability_scores}"]

    def pretty_classes(self, data: dict):
        pass

    def pretty_conditions(self, data: dict):
        effects = "\n  ".join(data['desc'])
        return [f"Name: {data['name']}", f'Effects:\n  {effects}'] 

    def pretty_damage_types(self, data: dict):
        return [f"Name: {data['name']}", f"Description: {data['desc'][0]}"]

    def pretty_equipment_categories(self, data: dict):
        list_equipment_catagories = []
        [list_equipment_catagories.append(catagory['name']) for catagory in data['equipment']]
        equipment_catagories = ", ".join(list_equipment_catagories)

        return [f"Name: {data['name']}", f"Equipment: {equipment_catagories}"]

    def pretty_equipment(self, data: dict):
        pass

    def pretty_features(self, data: dict):
        pass

    def pretty_languages(self, data: dict):
        list_data = []
        typical_speakers = ", ".join(data['typical_speakers'])
        
        list_data.append([
            f"Name: {data['name']}",
            f"Type: {data['type']}",
            f"Typical Speakers: {typical_speakers}",
            f"Script: {data['script']}"
        ])
        
        return list_data[0]


    def pretty_magic_items(self, data: dict):
        pass

    def pretty_magic_schools(self, data: dict):
        list_magic_schools = []
        [list_magic_schools.append(magic_school['name']) for magic_school in data['results']]
        magic_schools = ", ".join(list_magic_schools)

        return [f"Results: {data['count']}", f"Magic Schools: {magic_schools}"]

    def pretty_monsters(self, data: dict):
        pass

    def pretty_proficiencies(self, data: dict):
        pass

    def pretty_races(self, data: dict):
        pass

    def pretty_rules(self, data: dict):
        pass
    
    def pretty_rule_sections(self, data: dict):
        pass

    def pretty_skills(self, data: dict):
        pass

    def pretty_spells(self, data: dict):
        pass

    def pretty_starting_equipment(self, data: dict):
        pass

    def pretty_subclasses(self, data: dict):
        pass

    def pretty_subraces(self, data: dict):
        list_data = []
        list_keys = data.keys()

        try:
            list_ability_bonuses = []
            [list_ability_bonuses.append(f"{str(data['ability_bonuses'][ability_bonus]['bonus'])} to {data['ability_bonuses'][ability_bonus]['ability_score']['name']}") for ability_bonus in range(len(data['ability_bonuses']))]
            ability_bonuses = ", ".join(list_ability_bonuses)
        except:
            ability_bonuses = "None"
        try:
            list_starting_proficiencies = []
            [list_starting_proficiencies.append(proficiency['name']) for proficiency in data['starting_proficiencies']]
            starting_proficiencies = ", ".join(list_starting_proficiencies)
        except:
            starting_proficiencies = "None"
        try:
            list_language_options = []
            [list_language_options.append(option['name']) for option in data['language_options']['from']]
            language_options = ", ".join(list_language_options)
        except:
            language_options = "None"
        try:
            list_racial_traits = []
            [list_racial_traits.append(trait['name']) for trait in data['racial_traits']]
            racial_traits = ", ".join(list_racial_traits)
        except:
            racial_traits = "None"
        try:
            list_racial_trait_options = []
            [list_racial_trait_options.append(trait_option['name']) for trait_option in data['racial_trait_options']['from']]
            racial_trait_options = ", ".join(list_racial_trait_options)
        except:
            racial_trait_options = "None"

        list_data.append(f"Name: {data['name']}")
        list_data.append(f"Race: {data['race']['name']}")
        list_data.append(f"Description: {data['desc']}")
        if "ability_bonuses" in list_keys:
            list_data.append(f"Ability Bonuses: {ability_bonuses}")
        if "starting_proficiencies" in list_keys:
            list_data.append(f"Starting Proficiencies: {starting_proficiencies}")
        if "language_options" in list_keys:
            list_data.append(f"Languages: choose {data['language_options']['choose']} from {language_options}")
        if "racial_traits" in list_keys:
            list_data.append(f"Racial Traits: {racial_traits}")
        if "racial_trait_options" in list_keys:
            list_data.append(f"Racial Trait Options: choose {data['racial_trait_options']['choose']} from {racial_trait_options}")

        return list_data

    def pretty_traits(self, data: dict):
        pass

    def pretty_weapon_properties(self, data: dict):
        pass