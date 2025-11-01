s1 = int(input("Enter the First number : "))
s2 = int(input("Enter the Second number : "))

op = input("Enter the operator : ")

if(op == '+'):
    print(s1+s2)
elif(op == "-"):
    if(s1>s2):
        print(s1-s2)
    else:
        print(s2-s1)
elif(op == "*"):    
    print(s1*s2)

elif(op == "/"):    
    
    if(s1>s2):
        print(s1/s2)
    else:
        print(s2/s1)

else:
    print("invalid oparation....")


