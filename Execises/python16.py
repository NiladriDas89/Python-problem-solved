n=input("Enter the input: ")
def near_thousand(n):
  
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))