from multiprocessing import Process
import time
def ask_user():
    start=time.time()
    x=input("Enter your name")
    greet= f"Hello {x}"
    print(greet)
    print(f"ask_user time {time.time()-start}")

def complex_op():
    start=time.time();
    ls= [x**2 for x in range(20000000)]
    print(f"complex_op time taken is {time.time()-start}")


start=time.time()
ask_user()
complex_op()
print(f"Single thread Execution time {time.time()-start}")

process=Process(target=complex_op)
process.start()

ask_user()

process.join()

print(f"Two process involved")