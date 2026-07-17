def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

hi=outer_func("Hi")
bye=outer_func("Bye")


hi()
bye()

