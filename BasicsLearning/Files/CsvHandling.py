
file=open('TextFIles/csv.txt','r')
ls=file.readlines()

ls= [l.strip() for l in ls[1:]]
file.close()
print(ls)



