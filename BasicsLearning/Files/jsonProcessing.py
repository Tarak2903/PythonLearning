import json


file = open('TextFIles/friends_json.txt','r')

file_content=json.load(file)

print(file_content)

file.close()
