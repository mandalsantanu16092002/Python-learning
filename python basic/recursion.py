#when a function calls itself repeatedly

def fact(n):
    if(n==0 or n == 1):
        return 1
    else:
        return n*fact(n-1)   
#print(fact(6))


def sum(m):

    if(m==0):
        return 0
    return sum(m-1) + m

print(sum(5))