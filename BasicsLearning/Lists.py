friends=["Punit","KJ"]
wallpaper=["Chair",True,1]  #Also possible but not recommended
print(friends)
print(len(friends))


twoD=[["jake","amy"],["charles","vivian","Nikolaj"]]

print(len(twoD))

print(len(twoD[1]))

twoD.append(["Terry","Sharon"])

print(twoD)


list=[1,2,3,4]
sum=sum(list)
print(sum)

list1=["Amy","Holt"]
proper_list= ",".join(list1)
print(proper_list)

count=1
for friend in friends:
    print(f"This is my {friend} number {count}")
    count=count+1


'''
List Comprehension
'''

ls=[1,2,3,5,4]


new_ls= [i* 2 for i in range(5)]

print(new_ls)


ages=[1,2,3,4,5]

odd_ages= [i for i in ages if i%2==1]

print(odd_ages)