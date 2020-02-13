with open('demo.txt', 'r') as f:
	f_contents = f.read() # READ WHOLE FILE AT ONCE
	print(f_contents)
print(f.closed)

print('------------------------------------------------------------------')


with open('demo.txt','r') as f:
	for line in f:
		print(line,end = '')


print('-------------------------------------------------------------------')

