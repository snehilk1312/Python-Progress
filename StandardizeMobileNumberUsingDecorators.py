def wrapper(f):
    def fun(l):
        m=[]
        for i in l:
            if len(i)==11:
                i='+91 '+i[1:6]+' '+i[6:]
                m.append(i)
            elif len(i)==12:
                i='+91 '+i[2:7]+' '+i[7:]
                m.append(i)
            elif len(i)==13:
                i='+91 '+i[3:8]+' '+i[8:]
                m.append(i)
            elif len(i)==10:
                i='+91 '+i[0:5]+' '+i[5:]
                m.append(i)
        return f(m)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
#sort_phone=wrapper(sort_phone)

l = [input() for _ in range(int(input()))]
sort_phone(l)
