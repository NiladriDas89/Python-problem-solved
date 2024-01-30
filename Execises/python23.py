def substring_copy(text,n):
    flen=2
    if flen>len(text):
        flen=len(text)
    sub=text[:flen]
    res=""
    for hj in range(n) :
        res=res+sub
        
        return res

print(substring_copy(input("Enter your string here: "),int(input("Enter your number here "))))
