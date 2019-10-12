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
