def badly_formatted_function( x,y ):
    z=x+y
    return      z

def missing_type_hints(a, b):
    return a * b

def security_issue():
    user_input = input("Enter command: ")
    import os
    os.system(user_input)  # Bandit will catch this security issue

class BadlyFormattedClass:
    def __init__(self,name):
        self.name=name
    
    def do_something(self,x):return x+1
