'''def swap_case(s):
    t=[i.upper() if i.islower() else i.lower() for i in s]
    k=''.join(t)
    return k
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
  '''


def swap_case(s):
    t=''
    for i in s:
        if i.isupper():
            l=i.lower()
            t=t+l
        if i.islower():
            l=i.upper()
            t=t+l
        if not i.isalpha():
            t=t+i
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
