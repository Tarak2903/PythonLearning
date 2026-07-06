#By default all inputs that are taken are strings

x=input("What is your age\n")

print(x*12)  # prints age three times


#Correct Way

x= int(input("Whats the actually integer age"))
print(f"You have lived {x*12} months")