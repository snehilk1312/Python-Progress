def decor_fun(original_fun):
    def wrapper_fun():
        return original_fun()
    return wrapper_fun
def display():
    print('Executing display')
decorated_display=decor_fun(display)
decorated_display()
