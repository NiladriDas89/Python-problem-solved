''' 
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import *

dr=date(2014, 7, 2)
dt=date(2014, 7, 11)
gh=dt-dr
print(gh.days)