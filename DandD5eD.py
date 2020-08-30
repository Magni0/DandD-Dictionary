import json
import requests

# str mutate not working


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
    for key in res:
        if type(res[key]) == dict:
            for x in res[key]:
                print(key, " : ", res[key][x], "\n")
        print(key, " : ", res[key], "\n")

# mutates str to fit api convention
def mutate_input(item):
    item.lower()
    item.replace(" ", "-")
    return item


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

def item_select():
        print("input the spell/item/monster etc")
        choice_item = input("")
        if choice_item == "close":
            exit()
        return choice_item

while True:
    print("input 'close' to exit")
    section = section_select()
    item = item_select()
    search(section, item)
