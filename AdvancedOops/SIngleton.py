class Logger:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            print("Creating a logger")
            cls._instance=super().__new__(cls)
        return cls._instance

l1=Logger()
l2=Logger()
l3=Logger()
l4=Logger()
l5=Logger()