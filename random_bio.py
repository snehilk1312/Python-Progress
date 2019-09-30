import random
first=['john','mike','lola','amish','clark','modi','mitti','ramu','bengali']
last=['doe','doll','jagger','kramer','seinfield','cooper','hoffstader']
city=['king\'s landing','Metropolis','Hells kitchen','Gotham','Apollo','Thymescira' ]
state=['bihar','kerela','goa','delhi','punjab','bengal','assam']
for i in range(10):
    name1=random.choice(first)
    name2=random.choice(last)
    phone=f'+91 {random.randint(6000000000,9900000000)}'
    c=random.choice(city)
    s=random.choice(state)
    print(name1,name2,phone,c,s,sep='\n',end='\n_____________________________\n')
