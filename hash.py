#HASH FUNCTION


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l=[]
    for i in integer_list:
        l.append(i)
    t=tuple(l)
print(hash(t))
