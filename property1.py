class Job:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    @property
    def email(self):
        return self.first+'.'+self.last+'@email.com'
    @fullname.setter
    def fullname(self,name):
        first,last=name.split()
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('Instance deleted')
        self.first=None
        self.last=None
emp_1=Job('snehil','kumar')
print(emp_1.fullname)
print(emp_1.email)
emp_1.first='lola'
print(emp_1.email)
emp_1.fullname='mithun mohandas'
print(emp_1.email)
print(emp_1.first)
print(emp_1.last)
del emp_1.fullname
print(emp_1.first)
