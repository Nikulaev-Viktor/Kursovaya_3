from src.func import json_encode, last_five_operations, get_data_format

data = json_encode()
data = last_five_operations(data)
get_data_format(data)
#for i in last_five_operations(data)[5]:
print(get_data_format(data))
