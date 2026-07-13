class StopIteration1(Exception):
    def __init__(self,message):
        super.__init__(message)

class FirsHundredGenerator:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number<100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration1("Value crossed 3 man !!!")

g=FirsHundredGenerator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))


'''-----------------------------------------------Iterator-----------------------------------------------------------------'''
''' This is not an iterableeeee!!!!!!!!'''
class FirstFiveIterator:
    def __init__(self):
        self.numbers=[1,2,3,4,5,6]
        self.i=0
    def __next__(self):
        current=self.numbers[self.i]
        self.i+=1
        return current

it= FirstFiveIterator()

print(next(it))


