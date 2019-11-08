import math
from myfunctions import closestFactor,seriesSum,findFactors

def factorSum(n):
    factors=[]
    sqrt=math.sqrt(n)
    limit=int(sqrt)+1
    result=0
    if sqrt % 1==0:
        result+=sqrt
        limit-=1
    for i in range(2,limit):
        if n%i==0:
            result+=i+n/i
    return result

def customSeriesSum(a,b):
    if a!=b:
        return (a+b)*2

    return (a+b)

result=0
limit=10**8
secondLimit=int(math.sqrt(limit))
# result+=seriesSum(1,limit,1)
# result+=limit-1
for i in range(1,limit+1) :
        result+=int(limit/i)*i

print(result)
for real in range(1,secondLimit+1):
    for i in range(1,real+1):
       denominator=i*i+real*real
       if math.gcd(real,i)==1 :
            j=1
            value=customSeriesSum(real,i)
            while denominator*j<=limit:
                result+=j*value*int(limit/(denominator*j))
                j+=1
print(result)

        