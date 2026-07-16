import time
from threading import Thread

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

# start=time.time()
# ask_user()
# complex_op()
# print(f"Single Thread Execution time {time.time()-start}")


thread1=Thread(target=ask_user)
thread2=Thread(target=complex_op)

start=time.time()
thread1.start()
thread2.start()
print("My program ends")
thread1.join()
thread2.join()


print(f"Two Threads Execution time {time.time()-start}")