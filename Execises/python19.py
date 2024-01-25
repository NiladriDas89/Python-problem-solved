tmp="Is"
string1=str(input("Enter any type of string here: "))
if len(string1) >=2 and string1[:2]==tmp:
    print(string1)
else:
    print(tmp+" "+string1)