def duplicate_count(text):
    text=text.lower()
    l=[]
    j=set()
    flag=0
    for i in text:
        if not i.isalpha() or i.isnumeric():
            pass
        l.append(i)
    l.sort()
    for i in l:
        if  l.index(i)!=len(l)-1:
            if l[l.index(i)]==l[l.index(i)+1]:
                flag=1
                j.add(i)
            else:
                flag=0
        else:
            if l[l.index(i)]==l[l.index(i)-1] and l[l.index(i)-1]!=l[l.index(i)-2]:
                flag=1
                j.add(i)
            else:
                flag=0                
            
    return len(j)
text=input()
print(duplicate_count(text))

        
            
            
        
     
