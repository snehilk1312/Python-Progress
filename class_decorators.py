class counted(object):
    """ counts how often a function is called """
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)


@counted
def something():
    pass

something()
print(something.counter)
something()
print(something.counter)
something()
print(something.counter)
