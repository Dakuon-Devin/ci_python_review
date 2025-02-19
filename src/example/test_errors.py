def badly_formatted_function( x,y ):  # Black and Ruff should catch this
    z=x+y
    return      z

def missing_type_hints(a, b):  # MyPy should catch this
    return a * b

def security_issue():  # Bandit should catch this
    user_input = input("Enter command: ")
    import os
    os.system(user_input)
