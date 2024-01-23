''' Write a Python program that accepts a sequence of comma-separated numbers from the 
user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

val=input("Ente the value")
list=val.split(",")
print(list)
tuple=tuple(list)
print(tuple)






