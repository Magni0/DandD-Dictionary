
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
        list_magic_items = []
        [list_magic_items.append(magic_item['name']) for magic_item in data['results']]
        magic_items = "\n  - ".join(list_magic_items)

        return [f"Results: {data['count']}", f"Magic Items:\n  - {magic_items}"]

    def pretty_magic_schools(self, data: dict):
        list_magic_schools = []
        [list_magic_schools.append(magic_school['name']) for magic_school in data['results']]
        magic_schools = ", ".join(list_magic_schools)

        return [f"Results: {data['count']}", f"Magic Schools: {magic_schools}"]

    def pretty_monsters(self, data: dict):
        list_data = []
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

        list_speed = []
        if data['speed']['walk']:
            list_speed.append(f"Walk: {data['speed']['walk']}")
        if data['speed']['fly']:
            list_speed.append(f"Fly: {data['speed']['fly']}")
        if data['speed']['swim']:
            list_speed.append(f"Swim: {data['speed']['swim']}")
        speed = "\n  ".join(list_speed)
        list_data[0].append(f"Speed:\n  {speed}")

        list_stats = []
        list_stats.append([
            f"STR: {str(data['strength'])}",
            f"DEX: {str(data['dexterity'])}",
            f"CON: {str(data['constitution'])}",
            f"INT: {str(data['intelligence'])}",
            f"WIS: {str(data['wisdom'])}",
            f"CHA: {str(data['charisma'])}"
        ])
        stats = "\n  ".join(list_stats[0])
        list_data[0].append(f"Stats:\n  {stats}")

        list_monster_proficiencies = []
        [list_monster_proficiencies.append(f"{proficiency['proficiency']['name']}") for proficiency in data['proficiencies']]
        monster_proficiencies = "\n  ".join(list_monster_proficiencies)
        list_data[0].append(f"Proficiencies:\n  {monster_proficiencies}")

        damage_vulnerabilities = "\n  ".join(data['damage_vulnerabilities'])
        list_data[0].append(f"Damage Vulnerabilities:\n  {damage_vulnerabilities}")

        damage_resistances = "\n  ".join(data['damage_resistances'])
        list_data[0].append(f"Damage Resistances:\n  {damage_resistances}")

        damage_immunities = "\n  ".join(data['damage_immunities'])
        list_data[0].append(f"Damage Immunities:\n  {damage_immunities}")

        condition_immunities = "\n  ".join(data['condition_immunities'])
        list_data[0].append(f"Condition Immunities:\n  {condition_immunities}")

        list_senses = []
        senses_keys = data['senses'].keys()
        if "passive_perception" in senses_keys:
            list_senses.append(f"Passive Perception: {str(data['senses']['passive_perception'])}")
        if "darkvision" in senses_keys:
            list_senses.append(f"Dark Vision: {data['senses']['darkvision']}")
        if "blindsight" in senses_keys:
            list_senses.append(f"Blind Sight: {data['senses']['blindsight']}")
        senses = "\n  ".join(list_senses)
        list_data[0].append(f"Senses:\n  {senses}")

        list_data[0].append(f"Languages: {data['languages']}")
        list_data[0].append(f"Challenge Rating: {str(data['challenge_rating'])}")
        list_data[0].append(f"XP: {str(data['xp'])}")

        if "special_abilities" in list_keys:
            list_special_abilities = []
            for ability in data['special_abilities']:
                if "usage" in ability.keys():
                    list_special_abilities.append(f"Name: {ability['name']}\n    Description: {ability['desc']}\n    Can Use: {ability['usage']['times']} times {ability['usage']['type']}")
                else:
                    list_special_abilities.append(f"Name: {ability['name']}\n    Description: {ability['desc']}")
            special_abilities = "\n  ".join(list_special_abilities)
            list_data[0].append(f"Special Abilities:\n  {special_abilities}")

        if "actions" in list_keys:
            list_actions = []
            for action in data['actions']:
                if "usage" in action.keys():
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}\n    {action['usage']['type']} with {action['usage']['dice']} above {str(action['usage']['min_value'])}")
                elif "options" in action.keys():
                    list_options = []
                    for option in action['options']['from'][0]:
                        list_options.append(f"Name: {option['name']}, Count: {str(option['count'])}, Type: {option['type']}")
                    options = "\n      ".join(list_options)
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}\n    Choose {str(action['options']['choose'])} from:\n      {options}")
                else:
                    list_actions.append(f"Name: {action['name']}\n    Description: {action['desc']}")
            actions = "\n  ".join(list_actions)
            list_data[0].append(f"Actions:\n  {actions}")

        # legendary actions
        if "legendary_actions" in list_keys:
            list_legendary_actions = []
            for legendary_action in data["legendary_actions"]:
                list_legendary_actions.append(f"Name: {legendary_action['name']}\n    Description: {legendary_action['desc']}")
            legendary_actions = "\n  ".join(list_legendary_actions)
            list_data[0].append(f"Legendary Actions:\n  {legendary_actions}")

        return list_data[0]

    def pretty_proficiencies(self, data: dict):
        list_proficiencies = []

        list_proficiencies.append([
            f"{data['name']}",
            f"Details At Section: {data['references'][0]['type']}"
        ])

        return list_proficiencies

    def pretty_races(self, data: dict):
        pass

    def pretty_rules(self, data: dict):
        list_rules = []
        [list_rules.append(rule['name']) for rule in data['subsections']]
        rules = ", ".join(list_rules)

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
        list_data = []
        list_keys = data.keys()

        list_data.append(f"Name: {data['name']}")
        list_data.append(f"Race: {data['race']['name']}")
        list_data.append(f"Description: {data['desc']}")

        if "ability_bonuses" in list_keys:
            list_ability_bonuses = []
            [list_ability_bonuses.append(f"{str(data['ability_bonuses'][ability_bonus]['bonus'])} to {data['ability_bonuses'][ability_bonus]['ability_score']['name']}") for ability_bonus in range(len(data['ability_bonuses']))]
            ability_bonuses = ", ".join(list_ability_bonuses)
            list_data.append(f"Ability Bonuses: {ability_bonuses}")

        if "starting_proficiencies" in list_keys:
            list_starting_proficiencies = []
            [list_starting_proficiencies.append(proficiency['name']) for proficiency in data['starting_proficiencies']]
            starting_proficiencies = ", ".join(list_starting_proficiencies)
            list_data.append(f"Starting Proficiencies: {starting_proficiencies}")

        if "language_options" in list_keys:
            list_language_options = []
            [list_language_options.append(option['name']) for option in data['language_options']['from']]
            language_options = ", ".join(list_language_options)
            list_data.append(f"Languages: choose {data['language_options']['choose']} from {language_options}")

        if "racial_traits" in list_keys:
            list_racial_traits = []
            [list_racial_traits.append(trait['name']) for trait in data['racial_traits']]
            racial_traits = ", ".join(list_racial_traits)
            list_data.append(f"Racial Traits: {racial_traits}")

        if "racial_trait_options" in list_keys:
            list_racial_trait_options = []
            [list_racial_trait_options.append(trait_option['name']) for trait_option in data['racial_trait_options']['from']]
            racial_trait_options = ", ".join(list_racial_trait_options)
            list_data.append(f"Racial Trait Options: choose {data['racial_trait_options']['choose']} from {racial_trait_options}")

        return list_data

    def pretty_traits(self, data: dict):
        pass

    def pretty_weapon_properties(self, data: dict):
        pass