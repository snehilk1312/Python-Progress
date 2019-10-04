class Employee:
    raise_amount=1.2
    def __init__(self,name,alias,pay):
        self.name=name
        self.alias=alias
        self.pay=pay
    def display(self):
        print(self.name,self.alias,self.pay,sep='\t'*2,end='\n')
emp_1=Employee('snehil','steppenwolf',100000)
emp_2=Employee('Herman','Hesse',1000000)
emp_1.display()
emp_2.display()

print('_________________________MY LIFE IS A COMEDY_________________________')
Employee.display(emp_1)
Employee.display(emp_2)

