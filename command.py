#This program shi\ows the work performed
#upon the list on entering certain strings as command.


if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        k=input()
        if k.split()[0]=='insert':
            l.insert(int(k.split()[1]),int(k.split()[2]))
        elif k.split()[0]=='remove':
            l.remove(int(k.split()[1]))
        elif k.split()[0]=='append':
            l.append(int(k.split()[1]))
        elif k=='print':
            print(l)
        elif k=='sort':
            l.sort()
        elif k=='pop':
            l.remove(l[-1])
        elif k=='reverse':
            l.reverse()
