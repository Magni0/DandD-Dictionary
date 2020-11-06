from request_from_api import ApiRequest
from functions import Functions

req = ApiRequest()
func = Functions()

# test
data = req.section_list()
print(type(data))
list_data = func.dict_to_list_of_keys(data)
print(type(list_data))