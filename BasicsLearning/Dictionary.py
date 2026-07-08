dictionary={"Tarak":21,"KJ":21,"Harsh":20}

dictionary["Saurabh"]=23
print(dictionary)
print(dictionary["Tarak"])


# Order is maintained in Dictionary which is not maintained in Set
# No duplicate is allowed in Dictionary as well


for friends in dictionary:
    print(friends)
    print(dictionary[friends])


'''-----------------------------------------------------Dictionary Comprehension-----------------------------------------------'''


friends=["Punit","KJ","Mansi","Harsh"]
time_Seen=[1,2,3,4]


time_friends={
    friends[i]:time_Seen[i]
    for i in range(len(friends))
    if(time_Seen[i]<4)
}
print(time_friends)

timer_op= dict(zip(friends,time_Seen))
print(timer_op)

ls=list(range(len(friends)))

ans=list(zip(friends,ls))
print(ans)

