import os
from datetime import datetime
os.mkdir('demo_dir1')				#we cant make deep directory here
os.makedirs('demo_dir2/demo_subdir')		#we can make deep directory here

print(os.getcwd())

print(os.listdir())


os.rmdir('demo_dir1')
os.removedirs('demo_dir2/demo_subdir')

print(os.listdir())

#os.rename('test.txt', 'demo.txt')

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


for dirpath,dirnames,filenames in os.walk(os.getcwd()):
	print('Current Path: ', dirpath)
	print('directories: ', dirnames)
	print('Files: ', filenames)
	print()


print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)


print(os.path.basename('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))			# gives false if files doesn't exist



print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))
