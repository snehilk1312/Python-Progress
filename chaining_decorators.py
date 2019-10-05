def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star#is equivalent to
@percent
def printer(msg):     #def printer(msg):
    print(msg)        #     print(msg)
printer("Hello")      #printer=star(percent(printer))
                      #printer('Hello')
