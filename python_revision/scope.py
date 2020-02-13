x ='global _x'

def x_value():
	global x
	x = 'local x'
	print(x)


print(x)

x_value()


print(x)
