

def prime_generator(bound):
    # your code starts here (delete the pass):
    for i in range(2, bound):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if not flag:
            yield i



g=prime_generator(100)
print(next(g))
print(list(g))
