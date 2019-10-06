'''
Let's use decorators to build a name directory! You are given some information about N people.
Each person has a first name, last name, age and sex. 
Print their names in a specific format sorted by their age in ascending order
i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.
SAMPLE INPUT:
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

SAMPLE OUTPUT:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''
import operator
m=[]
def person_lister(f):
    def inner(people):
        #print(people)
        people.sort(key=lambda x:int(x[2]))
        #print(people)
        for i in people:
            k=f(i)
            m.append(k)
        return m
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
