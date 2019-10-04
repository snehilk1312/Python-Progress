class Employee:
    raise_amount=1.2
    def __init__(self,name,alias,pay):
        self.name=name
        self.alias=alias
        self.pay=pay
    def display(self):
        print(self.name,self.alias,self.pay,sep='\t'*2,end='\n')
    def apply_raise(self):
        self.pay*=Employee.raise_amount#or can use self.raise_amount
emp_1=Employee('snehil','steppenwolf',100000)
emp_2=Employee('Herman','Hesse',1000000)
emp_1.display()
emp_2.display()

print('_________________________MY LIFE IS A COMEDY_________________________')
emp_1.apply_raise()
Employee.display(emp_1)
Employee.display(emp_2)
print('_________________________MY LIFE IS A COMEDY_________________________')
print(emp_1.raise_amount)
print(Employee.raise_amount)
