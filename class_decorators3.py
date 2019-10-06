# Python program showing 
# class decorator with *args 
# and **kwargs 
  
class MyDecorator: 
    def __init__(self, function): 
        self.function = function 
      
    def __call__(self, *args, **kwargs): 
  
        # We can add some code  
        # before function call 
        print('THIS LINE GOT EXECUTED BEFORE FUNCTION CALL')
        self.function(*args, **kwargs) 
        print('THIS LINE GOT EXECUTED AFTER FUNCTION CALL')
        # We can also add some code 
        # after function call. 
      
  
# adding decorator to the class  
@MyDecorator                                #function=MyDecorator(function)
def function(name, message ='Hello'): 
    print("{}, {}".format(message, name)) 
  
function("geeks_for_geeks", "hello")        #function.__call__('lola','cola')
