n=int(input('Enter the num:'))
def recurr(a):
    if a==1:
        return 1
    else:
        return a*recurr(a-1)
print(recurr(n))
