with open('test.txt', 'w') as f:
	f.write("Test Check")
	f.seek(1)
	f.write('Bat')
