from modules.request_from_api import ApiRequest
from modules.functions import Functions
from modules.pretty_list import PrettyList
from modules.saved_requests import SaveFileManager

req = ApiRequest()
func = Functions()
pl = PrettyList()
sfm = SaveFileManager()


print("Type 'exit' to exit:")
print("""
Welcome to the D&D Dictonary
Would you like to load a saved query or make a new query?
1: Open Saved Query
2: Make New Query
""")

query_choice = input("")
print("")

if query_choice == "1":
    # put code here
    pass

elif query_choice == "2":
    sections = pl.pretty_list_sections(req.list_sections())
    
    input_section = input("\nSelect section: ")
    func.check_exit(input_section)
    print("")
    
    if input_section in sections:
        section = pl.pretty_section_search(req.section_search(input_section))
        
        input_item = func.cap_input(input("\nSelect Item: "))
        func.check_exit(input_item)

        if input_item in section:
            # put code here
            pass
        
        else:
            raise Exception(f"Invalid input: {input_item} not in {input_section}")    
    
    else:
        raise Exception(f"Invalid input: {input_section} not in listed sections")

else:
    raise Exception("Invalid input: please select option 1 or 2")
