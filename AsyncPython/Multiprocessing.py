import time
from multiprocessing import Process

def user_input():
    start=time.time()
    name=input("Enter your name")
    print(f"Hello {name}")
    print(f"User input took {time.time()-start}")

def complex_op():
    start=time.time()
    ls=[l**2 for l in range(20000000)]
    print(f"Complex operation took {time.time()-start}")



p=Process(target=complex_op)

p2=Process(target=user_input)

p.start()
p2.start() 

