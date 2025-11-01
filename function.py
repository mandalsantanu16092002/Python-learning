string = input("Enter a name : ")

#p = int(string) 
# ---> string a number o string hisabe save hobe seta int a convert kora jabe (1234,423) 
# name hobe na (sanu,nmhhadi)
l = len(string)

def odd_even(a):
    if (a%2 == 0):
        print(string,"is a Even string")
    else:
        print(string,"is a odd string")

odd_even(l)
