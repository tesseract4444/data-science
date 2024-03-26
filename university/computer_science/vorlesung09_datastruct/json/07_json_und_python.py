import json

#string als json document
json_str: str = """{
	"key": "value",
	"array_key": ["string", "array"]
}"""

#json.loads liest string als json ein
json_dict = json.loads(json_str) #-> dictionary wird zurückgegeben
print(type(json_dict)) # <class 'dict'> 
print(json_dict['key']) # value

json_dict['object_key'] = {
	'other_value': False #weiteres dict mit z.b. other value false
}

json_str_new: str = json.dumps(json_dict, indent=2) #dumps exportiert python-wert als json exportieren zu string, indent macht jeden key in neue zeile mit einrückung von 2
print(json_str_new)

# {
# "key": "value",
# "array_key": [
# "string",
# "array"
# ],
# "object_key": {
# "other_value": false
# }
# }
