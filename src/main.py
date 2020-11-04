import json
import requests

sections = ("ability-scores",
"classes",
"conditions",
"damage-types",
"equipment-categories",
"equipment",
"features",
"languages",
"magic-schools",
"monsters",
"proficiencies",
"races",
"skills",
"spellcasting",
"spells",
"starting-equipment",
"subclasses",
"subraces",
"traits",
"weapon-properties")

# gets request from api and echos contents to screen
def search(section, item):
    r = requests.get(f"https://www.dnd5eapi.co/api/{mutate_input(section)}/{mutate_input(item)}/")
    res = json.loads(r.text)

    print("select what you wish to see or press enter to see all\n")
    for i in res.keys(): 
        print(i)

    choice = input("")

    print("\n")

    if choice:
        print(res[choice])
    
    else:
        print("tags with url show you the section and name of that thing to look up for more info eg. url: '/api/damage-types/acid' means section: damage-types index: acid")
        print(json.dumps(res, indent=1) + "\n")

# mutates str to fit api convention
def mutate_input(item):
    return item.lower().replace(" ", "-")

#
def section_select():
    print("input 'sections' to display a list of sections or input a section")
    choice_section = input("")

    if choice_section == "sections":
        for i in sections:
            print(i)
        section_select()

    elif choice_section == "close":
        exit()

    elif choice_section not in sections:
        print("The section inputed has either been misspelled or is not a section")
        section_select()

    return choice_section

# 
def item_select():
        print("input the index eg.spell/item/monster etc")
        choice_item = input("")

        if choice_item == "close":
            exit()

        return choice_item

# runs functions in correct sequence
while True:
    print("input 'close' to exit")
    section = section_select()
    item = item_select()
    search(section, item)
