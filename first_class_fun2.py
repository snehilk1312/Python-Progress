'''
This is a basic example of a first class functions
'''
def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text
my_fun=html_tag('p')
my_fun('This is the paragraph part!')
my_fun=html_tag('h')
my_fun('This is Header.')
