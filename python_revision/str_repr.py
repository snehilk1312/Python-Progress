s="""w'o"w"""
print(type(s))
print(str(s))
print(repr(s))
print(eval(repr(s)))

print('___________________________________________________________________________________')



import datetime
today=datetime.datetime.today()
print(str(today))
print(repr(today))
