rows,columns=list(map(int,input().split()))

for i in range(1,rows//2+1):
    print('-'*((columns-(2*i-1)*3)//2),(2*i-1)*'.|.','-'*((columns-(2*i-1)*3)//2),sep='',end='\n')
print(((columns-7)//2)*'-','WELCOME',((columns-7)//2)*'-',sep='')
i=rows//2
while i>0:
    print('-'*((columns-(2*i-1)*3)//2),(2*i-1)*'.|.','-'*((columns-(2*i-1)*3)//2),sep='',end='\n')
    i-=1
