from collections import OrderedDict
N = int(input())
ordered_dictionary=OrderedDict()
for i in range(N):
    my_list=list(input().split())
    a=' '.join(my_list[0:-1])
    b=my_list[-1]
    try :
        ordered_dictionary[a]=ordered_dictionary[a]+int(b)
    except:
        ordered_dictionary[a]=int(b)
for i in ordered_dictionary:
        print(i, ordered_dictionary[i])

