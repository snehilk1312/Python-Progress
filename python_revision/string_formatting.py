foo=1
bar='bar'
baz=3.14
print("{0}, {1}, {2}, and {1}".format(foo, bar, baz))


print("----------------------------------------------------------------------------")


class AssignValue:
	def __init__(self, value):
		self.value=value
my_value= AssignValue(input("Enter the Value to be assigned: "))
print("My entered value is : {0.value}".format(my_value))

print("----------------------------------------------------------------------------")


my_dict = {'key' :6, 'other_key' :7}

print("My other key is : {[other_key]}".format(my_dict))


print('----------------------------------------------------------------------------')


# map along with string formatting, by doing this
# we apply the given operation on every element of iterable.

t=[i for i in range(10)]
print(t)
print(list(map('The counting goes as : {}'.format, t)))

print('-----------------------------------------------------------------------------')

for i in range(10):
	print(f"The value is {i:02}")
