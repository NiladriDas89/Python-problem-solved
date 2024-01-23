'''
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
#__doc__ are using for Known the documentation
def docu():
    print(abs.__doc__)
docu()
    