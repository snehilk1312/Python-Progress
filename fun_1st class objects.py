def say_hello(arg):
    return 'hello {}'.format(arg)
def be_awesome(arg):
    return 'yo {},every {} is awesome.'.format(arg,arg)
def main_fun(greet):
    return greet('bob')
print(main_fun(say_hello))
print(main_fun(be_awesome))
