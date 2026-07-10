
def read_from_file(location):
    with open(location,'r') as file:
        return file.read()

def write_to_file(location,content):
    with open(location,'w')as file:
        file.write(content)