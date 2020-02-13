with open('demo.txt', 'r') as f:
	size_to_read = 10

	f_contents = f.read(size_to_read)
	print(f.tell())			#Displays the index where the pointer is actually

	print(f_contents)
	f.seek(0)			#Basically set the pointer at the specified position

	f_contents = f.read(size_to_read)
	print(f_contents)
