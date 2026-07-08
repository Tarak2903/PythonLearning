'''
1.Sets do not maintain any order
2.No duplicate elements 
'''


cops={"Jake","Amy","Charles","Terry"}

cops.add("Jake")

print(cops)

friends=["Rolf","ruth","charlie","Jen"]
guests=["jose","Bob","Rolf","Charlie","michael"]

friends_lower={ friend.lower() for friend in friends}

guests_lower={guest.lower() for guest in guests}

present_guests= guests_lower.intersection(friends_lower)


present_guests={ps.title() for ps in present_guests}

print(present_guests)