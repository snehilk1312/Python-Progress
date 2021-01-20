# This module provides access to the Unix shadow password database.

import spwd
import argparse

# print(spwd.getspall())
# print(spwd.getspall()[1])

parser = argparse.ArgumentParser(description="an useless program for unix shadow password database tutorial")
parser.add_argument('-u', '--user-name', action="store_true")
parser.add_argument('-p', '--hash-pw', action="store_true")
parsed = parser.parse_args()

if not (parsed.user_name or parsed.hash_pw):
        for i in spwd.getspall():
                print(i)

elif parsed.user_name and parsed.hash_pw:
        for i in spwd.getspall():
                print(f'user: {i[0]},   hash:{i[1]}')

elif parsed.hash_pw:
        for i in spwd.getspall():
                print(i[1])

else:
        # get login name
        for i in spwd.getspall():
                print(i[0])

print('*' * 150)


# getting password database entry for a given user name
print(spwd.getspnam('root'))
