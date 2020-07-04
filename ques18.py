import json 
my_info = {'name':'dipan','age':'22'}


to_json = json.dumps(my_info)

print(to_json)

to_dict = json.loads(to_json)
print(to_dict['name'] )