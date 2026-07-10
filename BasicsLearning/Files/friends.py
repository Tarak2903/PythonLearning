friends=input("Enter your Three Friends separated by space\n")

ls=friends.split(' ')
st=set(ls)

myfile=open('nearby_friends.txt', 'r')
nearby_friends=myfile.read()
print(nearby_friends)

st2=set(nearby_friends.split('\n'))

myfile.close()

myfile2=open('friends.txt', 'a')

near =st2.intersection(st)

for i in near:
    myfile2.write(i)
