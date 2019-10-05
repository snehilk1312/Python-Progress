def decorator_function(func):
    def new_func(c,d):
        if c<d:
            c,d=d,c
        return func(c,d)
    return new_func


@decorator_function
def div(a,b):
    print(a/b)
div(2,4)
