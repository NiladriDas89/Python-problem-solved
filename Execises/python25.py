def check_num(group_num,Num):
    tmp=list(group_num.split(","))
    for n in tmp:
        if Num==n:
            print("These value are exist on this group :",Num)
            return True
    return False


print(check_num(input("Enter the Listy of number: "),input("Your number: ")))      


