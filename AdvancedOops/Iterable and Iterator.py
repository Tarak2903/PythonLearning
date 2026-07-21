class Counter:
    def __init__(self,limit):
        self.limit=limit
        self.current=1
    def __next__(self):
        curr=self.current
        self.current+=1
        if self.current>self.limit:
            raise StopIteration
        return curr
    def __iter__(self):
        return self

c=Counter(100)

for i in c:
    print(i)