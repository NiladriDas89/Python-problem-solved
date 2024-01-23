'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
import sys 

n=int(input("Enter the integer:\t"))
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
print(n1+n2+n3)
'''
input are integer :5
convert the integer to string 5: ("%s"%n) through type casting
& int function are convert the string to integer
n2 are taking the integer at 2 time as a string & convert the code on integer so it will be  
55
reason: ("%s%s"%(n,n))
%s are represented the string on these (),So these %s has tow time & taking n as string & placing the int  are integer so output :55
Same as for n3 casuse there has 3 time %s so it output is : 555 
Then it sum are printing through Print function
print(n1+n2+n3)
Output :
615
'''
