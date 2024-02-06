def check(Num=input("Enter your number: ")):
    group=Num
    
    for ab in group:
         out=''
         time=ab
         while time>0:
             out+='*'
             time=time-1
    print(out)
            
            
