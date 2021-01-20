import pwd
import argparse

# print(pwd.getpwall())
# print(pwd.getpwall()[1])

parser = argparse.ArgumentParser(description="an useless program for password entry database tutorial")
parser.add_argument('-u', '--user-name', action="store_true")
parsed = parser.parse_args()

if not parsed.user_name:
	for i in pwd.getpwall():
        	print(i)

else:
	# get login name
	for i in pwd.getpwall():
        	print(i[0])

print('*' * 150)


# getting password database entry for a specific uid
print(pwd.getpwuid(3))

# getting password database entry for a given user name
print(pwd.getpwnam('root'))


