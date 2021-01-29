import grp
import operator

all_groups = grp.getgrall()
groups = sorted((g for g in all_groups), key=operator.attrgetter('gr_name'))

# print(groups)

# find the longest length for the name
name_length = max(len(g.gr_name) for g in groups) + 1

# string formatting pattern
fmt = '{: <{max_len}} {: >5} {: >10} {: >1}'

# Print header
print(fmt.format("Name", "GID", "Password","Members",max_len=name_length))

# Print the data
for g in groups:
        print(fmt.format(g.gr_name, g.gr_gid, g.gr_passwd,', '.join(g.gr_mem),max_len=name_length))
