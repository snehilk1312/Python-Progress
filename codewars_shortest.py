def find_short(s):
    count=0
    l=[]
    i=0
    while len(s)>=i+1:
        count+=1
        if s[i]==' ':
            count-=1
            l.append(count)
            count=0
        i+=1
    l.append(count)
    return min(l) # l: shortest word length
a='DarkCoin Ripple BTC'
print(len(a))
print(find_short(a))

