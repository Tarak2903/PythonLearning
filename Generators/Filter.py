
ls=["Rohan","Rahul","Tarak"]


best_friend= filter(lambda x: x.startswith('R'),ls)

print(next(best_friend))
print(next(best_friend))



best_friend=map(lambda r: r.lower(),ls)

print(next(best_friend))




