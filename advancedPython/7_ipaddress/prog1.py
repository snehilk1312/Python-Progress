import ipaddress
import random

print(ipaddress.ip_address("192.168.1.1"))


num1 = random.randint(1000000,1000000000)
print(ipaddress.ip_address(num1))


num2 = random.randint(4254076641128259285690398495165382,52540766411282592856903984951653826561)
print(ipaddress.ip_address(num2))
