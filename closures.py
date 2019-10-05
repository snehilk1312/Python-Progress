def outer_func():
    message='Hi'
    def inner_func():
        print(message)
    return inner_func
my_func=outer_func()
my_func()
print(my_func.__name__)
