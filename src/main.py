from modules.request_from_api import ApiRequest
from modules.functions import Functions
from modules.pretty_list import PrettyList
from modules.saved_requests import SaveFileManager
import sys

req = ApiRequest()
func = Functions()
pl = PrettyList()
sfm = SaveFileManager()

print("""
Welcome to the D&D Dictonary
Would you like to load a saved query or make a new query?
1: open saved query
2: make new query
""")

query_choice = input("")

if query_choice == "1":
    pass

elif query_choice == "2":
    print("\nSelect a section or type 'exit' to exit:")
    sections = func.pretty_section_list(req.section_list())
    section_choice = input("")
    if section_choice == "exit":
        sys.exit(0)
    elif section_choice in sections:
        print("\n")
        # work on pretty printing stuff
    else:
        raise Exception("Invalid input: please check spelling")

else:
    raise Exception("Invalid input: please select option 1 or 2")
