
class PrettySearch():
    def pretty_list_sections(self, data: dict):
        list_data = data.keys()
        for item in list_data:
            print(item)
        return list_data

    def pretty_section_search(self, data: dict):
        list_data: list = []
        print(f"Total count: {data['count']}")
        for name in data["results"]:
            print(name["name"])
            list_data.append(name["name"])
        return list_data

    # def pretty_specific_search(self, data):
    #     pass

class PrettyItem():
    def pretty_ability_scores(self, data: dict):
        list_ability_scores: list = []
        [list_ability_scores.append(score['name']) for score in data['results']]
        ability_scores: str = ", ".join(list_ability_scores)

        return [f"Results: {data['count']}", f"Ability Scores: {ability_scores}"]

    def pretty_classes(self, data: dict):
        list_classes: list = []
        list_keys = data.keys()

        list_classes.append(f"Name: {data['name']}")
        list_classes.append(f"Hit Die: {str(data['hit_die'])}")

        list_proficiency_choice: list = []
        [list_proficiency_choice.append(choice['name']) for choice in data['proficiency_choices'][0]['from']]
        proficiency_choices: str = "\n    - ".join(list_proficiency_choice)
        list_classes.append(f"Skill Proficiencies:\n  Choose {str(data['proficiency_choices'][0]['choose'])} from:\n    - {proficiency_choices}")

        proficiency: str = "\n  - ".join([prof['name'] for prof in data['proficiencies']])
        list_classes.append(f"Proficiencies:\n  - {proficiency}")

        saving_throws: str = "\n  - ".join([throw['name'] for throw in data['saving_throws']]) 
        list_classes.append(f"Saving Throws:\n  - {saving_throws}")

        subclasses: str = "\n  - ".join([subclass['name'] for subclass in data['subclasses']])
        list_classes.append(f"Subclasses:\n  - {subclasses}")

        list_spellcasting: list = []
        [list_spellcasting.append(f"- {info['name']}:\n      {info['desc'][0]}") for info in data['spellcasting']['info']]
        spellcasting: str = "\n  ".join(list_spellcasting)
        list_classes.append(f"Spellcasting Ability: {data['spellcasting']['spellcasting_ability']['name']}\nSpellcasting Info:\n  {spellcasting}")

        return list_classes

    def pretty_conditions(self, data: dict):
        effects: str = "\n  ".join(data['desc'])
        return [f"Name: {data['name']}", f'Effects:\n  {effects}'] 

    def pretty_damage_types(self, data: dict):
        return [f"Name: {data['name']}", f"Description: {data['desc'][0]}"]

    def pretty_equipment_categories(self, data: dict):
        list_equipment_catagories: list = []
        [list_equipment_catagories.append(catagory['name']) for catagory in data['equipment']]
        equipment_catagories: str = ", ".join(list_equipment_catagories)

        return [f"Name: {data['name']}", f"Equipment: {equipment_catagories}"]

    def pretty_equipment(self, data: dict):
        pass

    def pretty_features(self, data: dict):
        pass

    def pretty_languages(self, data: dict):
        list_data: list = []
        typical_speakers: str = ", ".join(data['typical_speakers'])
        
        list_data.append([
            f"Name: {data['name']}",
            f"Type: {data['type']}",
            f"Typical Speakers: {typical_speakers}",
            f"Script: {data['script']}"
        ])
        
        return list_data[0]

    def pretty_magic_items(self, data: dict):
        list_magic_items: list = []
        [list_magic_items.append(magic_item['name']) for magic_item in data['results']]
        magic_items: str = "\n  - ".join(list_magic_items)

        return [f"Results: {data['count']}", f"Magic Items:\n  - {magic_items}"]

    def pretty_magic_schools(self, data: dict):
        list_magic_schools: list = []
        [list_magic_schools.append(magic_school['name']) for magic_school in data['results']]
        magic_schools: str = ", ".join(list_magic_schools)

        return [f"Results: {data['count']}", f"Magic Schools: {magic_schools}"]

    def pretty_monsters(self, data: dict):
        list_data: list = []
        list_keys = data.keys()

        list_data.append([
            f"Name: {data['name']}",
            f"Size: {data['size']}",
            f"Type: {data['type']}",
            f"Subtype: {data['subtype']}",
            f"Alignment: {data['alignment']}",
            f"Armor Class: {str(data['armor_class'])}",
            f"Hit Points: {str(data['hit_points'])}",
            f"Hit Dice: {data['hit_dice']}"
        ])

        list_speed: list = []
        if data['speed']['walk']:
            list_speed.append(f"Walk: {data['speed']['walk']}")
        if data['speed']['fly']:
            list_speed.append(f"Fly: {data['speed']['fly']}")
        if data['speed']['swim']:
            list_speed.append(f"Swim: {data['speed']['swim']}")
        speed: str = "\n  ".join(list_speed)
        list_data[0].append(f"Speed:\n  {speed}")

        list_stats: list = []
        list_stats.append([
            f"STR: {str(data['strength'])}",
            f"DEX: {str(data['dexterity'])}",
            f"CON: {str(data['constitution'])}",
            f"INT: {str(data['intelligence'])}",
            f"WIS: {str(data['wisdom'])}",
            f"CHA: {str(data['charisma'])}"
        ])
        stats: str = "\n  ".join(list_stats[0])
        list_data[0].append(f"Stats:\n  {stats}")

        list_monster_proficiencies: list = []
        [list_monster_proficiencies.append(f"{proficiency['proficiency']['name']}") for proficiency in data['proficiencies']]
        monster_proficiencies: str = "\n  ".join(list_monster_proficiencies)
        list_data[0].append(f"Proficiencies:\n  {monster_proficiencies}")

        damage_vulnerabilities: str = "\n  ".join(data['damage_vulnerabilities'])
        list_data[0].append(f"Damage Vulnerabilities:\n  {damage_vulnerabilities}")

        damage_resistances: str = "\n  ".join(data['damage_resistances'])
        list_data[0].append(f"Damage Resistances:\n  {damage_resistances}")

        damage_immunities: str = "\n  ".join(data['damage_immunities'])
        list_data[0].append(f"Damage Immunities:\n  {damage_immunities}")

        condition_immunities: str = "\n  ".join(data['condition_immunities'])
        list_data[0].append(f"Condition Immunities:\n  {condition_immunities}")

        list_senses: list = []
        senses_keys = data['senses'].keys()
        if "passive_perception" in senses_keys:
            list_senses.append(f"Passive Perception: {str(data['senses']['passive_perception'])}")
        if "darkvision" in senses_keys:
            list_senses.append(f"Dark Vision: {data['senses']['darkvision']}")
        if "blindsight" in senses_keys:
            list_senses.append(f"Blind Sight: {data['senses']['blindsight']}")
        senses: str = "\n  ".join(list_senses)
        list_data[0].append(f"Senses:\n  {senses}")

        list_data[0].append(f"Languages: {data['languages']}")
        list_data[0].append(f"Challenge Rating: {str(data['challenge_rating'])}")
        list_data[0].append(f"XP: {str(data['xp'])}")

        if "special_abilities" in list_keys:
            list_special_abilities: list = []
            for ability in data['special_abilities']:
                if "usage" in ability.keys():
                    list_special_abilities.append(f"Name: {ability['name']}\n    Description: {ability['desc']}\n    Can Use: {ability['usage']['times']} times {ability['usage']['type']}")
                else:
                    list_special_abilities.append(f"Name: {ability['name']}\n    Description: {ability['desc']}")
            special_abilities: str = "\n  ".join(list_special_abilities)
            list_data[0].append(f"Special Abilities:\n  {special_abilities}")

        if "actions" in list_keys:
            list_actions: list = []
            for action in data['actions']:
                if "usage" in action.keys():
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}\n    {action['usage']['type']} with {action['usage']['dice']} above {str(action['usage']['min_value'])}")
                elif "options" in action.keys():
                    list_options: list = []
                    for option in action['options']['from'][0]:
                        list_options.append(f"Name: {option['name']}, Count: {str(option['count'])}, Type: {option['type']}")
                    options: str = "\n      ".join(list_options)
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}\n    Choose {str(action['options']['choose'])} from:\n      {options}")
                else:
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}")
            actions: str = "\n  ".join(list_actions)
            list_data[0].append(f"Actions:\n  {actions}")

        if "legendary_actions" in list_keys:
            list_legendary_actions: list = []
            for legendary_action in data["legendary_actions"]:
                list_legendary_actions.append(f"Name: {legendary_action['name']}\n    Description: {legendary_action['desc']}")
            legendary_actions: str = "\n  ".join(list_legendary_actions)
            list_data[0].append(f"Legendary Actions:\n  {legendary_actions}")

        return list_data[0]

    def pretty_proficiencies(self, data: dict):
        list_proficiencies: list = []

        list_proficiencies.append([
            f"{data['name']}",
            f"Details At Section: {data['references'][0]['type']}"
        ])

        return list_proficiencies

    def pretty_races(self, data: dict):
        pass

    def pretty_rules(self, data: dict):
        list_rules: list = []
        [list_rules.append(rule['name']) for rule in data['subsections']]
        rules: str = ", ".join(list_rules)

        return [f"Name: {data['name']}", f"Subsections: {rules}"]
    
    def pretty_rule_sections(self, data: dict):
        return [f"Name: {data['name']}", f"{data['desc']}"]

    def pretty_skills(self, data: dict):
        pass

    def pretty_spells(self, data: dict):
        pass

    def pretty_starting_equipment(self, data: dict):
        pass

    def pretty_subclasses(self, data: dict):
        pass

    def pretty_subraces(self, data: dict):
        list_data: list = []
        list_keys = data.keys()

        list_data.append(f"Name: {data['name']}")
        list_data.append(f"Race: {data['race']['name']}")
        list_data.append(f"Description: {data['desc']}")

        if "ability_bonuses" in list_keys:
            list_ability_bonuses: list = []
            [list_ability_bonuses.append(f"{str(data['ability_bonuses'][ability_bonus]['bonus'])} to {data['ability_bonuses'][ability_bonus]['ability_score']['name']}") for ability_bonus in range(len(data['ability_bonuses']))]
            ability_bonuses: str = ", ".join(list_ability_bonuses)
            list_data.append(f"Ability Bonuses: {ability_bonuses}")

        if "starting_proficiencies" in list_keys:
            list_starting_proficiencies: list = []
            [list_starting_proficiencies.append(proficiency['name']) for proficiency in data['starting_proficiencies']]
            starting_proficiencies: str = ", ".join(list_starting_proficiencies)
            list_data.append(f"Starting Proficiencies: {starting_proficiencies}")

        if "language_options" in list_keys:
            list_language_options: list = []
            [list_language_options.append(option['name']) for option in data['language_options']['from']]
            language_options: str = ", ".join(list_language_options)
            list_data.append(f"Languages: choose {data['language_options']['choose']} from {language_options}")

        if "racial_traits" in list_keys:
            list_racial_traits: list = []
            [list_racial_traits.append(trait['name']) for trait in data['racial_traits']]
            racial_traits: str = ", ".join(list_racial_traits)
            list_data.append(f"Racial Traits: {racial_traits}")

        if "racial_trait_options" in list_keys:
            list_racial_trait_options: list = []
            [list_racial_trait_options.append(trait_option['name']) for trait_option in data['racial_trait_options']['from']]
            racial_trait_options: str = ", ".join(list_racial_trait_options)
            list_data.append(f"Racial Trait Options: choose {data['racial_trait_options']['choose']} from {racial_trait_options}")

        return list_data

    def pretty_traits(self, data: dict):
        list_data: list = []

        list_data.append(f"Name: {data['name']}")
        list_data.append(f"Description: {data['desc'][0]}")
        
        list_races_available: list = []
        [list_races_available.append(race['name']) for race in data['races']]
        races_available: str = ", ".join(list_races_available)
        list_data.append(f"Races available: {races_available}")

        list_subraces_available: list = []
        [list_subraces_available.append(subrace['name']) for subrace in data['subraces']]
        subraces_available: str = ", ".join(list_subraces_available)
        list_data.append(f"Subraces available: {subraces_available}")

        list_proficiencies: list = []
        [list_proficiencies.append(prof['name']) for prof in data['proficiencies']]
        proficiencies: str = ", ".join(list_proficiencies)
        list_data.append(f"Proficiencies: {proficiencies}")

        try:
            list_proficiency_choices: list = []
            [list_proficiency_choices.append(choice['name']) for choice in data['proficiency_choices']['from']]
            choices: str = ", ".join(list_proficiency_choices)
            list_data.append(f"Proficiency choices:\n  Choose: {data['proficiency_choices']['choose']} {data['proficiency_choices']['type']} from {choices}")
        except:
            list_data.append("Proficiency choices:")

        return list_data

    def pretty_weapon_properties(self, data: dict):
        list_data: list = []

        list_data.append(f"Name: {data['name']}")
        list_data.append(f"Description: {data['desc'][0]}")

        return list_data
