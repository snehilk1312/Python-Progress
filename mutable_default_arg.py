'''
common gotchas in python

'''
def append_to( element,self=[]):
        self.append(element)
        return self

#my_list=[19]
print(append_to(12))
print(append_to(42))


# output: 

#[12]
#[12, 42]
