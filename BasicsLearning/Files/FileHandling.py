my_file=open('TextFIles/data.txt', 'r')
file_content=my_file.read()
my_file.close()

print(file_content)

user=input("Enter your name please")
my_file_writing=open('TextFIles/data.txt', 'w')

my_file_writing.write(user)

my_file_writing.close()

