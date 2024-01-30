

liste =[1, 4, 6, 4, 7, 4]

def lis(num):
    count=0
    for n in num:
        if n==4:
            count=count+1
    return count



print(lis(liste))
