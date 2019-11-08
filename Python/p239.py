import math

def combination(n,r):
    result=1
    for i in range(n-r+1,n+1):
        result*=i
    return result/math.factorial(r)

def derangement(n,r):
    if( n < 1 ):
        return math.factorial(r)
    n = n - 1
    result = r * derangement( n , r )
    if n>0:
        result+= n * derangement( n-1 , r + 1)
    return result

a = math.factorial(100)
b =  combination(25,3)
c=derangement(22,75)
print("{:.12f}".format(float(b*c/a)))
print(b,c)

## Need to understand this more