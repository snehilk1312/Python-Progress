class MyDecorator: 
    def __init__(self, function): 
        self.function = function 
      
    def __call__(self): 
  
        # We can add some code  
        # before function call
        print("WE ARE INSIDE  __CALL__ METHOD")
  
        self.function()
  
        # We can also add some code 
        # after function call. 
        print('self.function() got executed')
  
# adding decorator to the class  
@MyDecorator                         #function=MyDecorator(function)
def function():                      #by writing above statement we created an instance 
    print("GeeksforGeeks")           #execution of __call__
function()
