import json
file=open('TextFIles/csv_file.txt','r')

file_content= file.readlines()

file_content= [f.strip() for f in file_content]


ans_ls=[]

for line in file_content:
    ls=line.split(',')
    d= {"club":f"{ls[0]}","country":f"{ls[1]}","city":f"{ls[2]}"}
    ans_ls.append(d)

jsonfile=open("TextFIles/json_file.txt", 'w')
json.dump(ans_ls,jsonfile)
jsonfile.close()