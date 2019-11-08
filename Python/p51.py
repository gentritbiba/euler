import math

def isPrime(n):
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n)),2):
        if n%i==0:
            # print(i)
            return False
    return True

def generatePrimes(low,high):
    primeArr=[]
    for i in range(low,high):
        if isPrime(i):
            primeArr.append(i)
    return primeArr

def repChar(a,b,c):
    a=list(a)
    a[b]=str(c)
    a="".join(a)
    return a

# breakloop=False
# for i in range (100000,200000):
#     print(i)
#     a=str(i)
#     for j in range(0,len(a)):
#         for k in range(j+1,len(a)):
#             for ii in range(k+1,len(a)):
#                 count=0
#                 for l in range(0,10):
#                     b=a
#                     b=repChar(b,j,l)
#                     b=repChar(b,k,l)
#                     b=repChar(b,ii,l)
#                     # print(b)
#                     # print(int(b))
#                     if isPrime(int(b)) and len(str(int(b)))==len(a):
#                         # print(b)
#                         count=count+1
#                         # print(count,b)
#                         if count==8:
#                             breakloop=True
#                             print(a,j,k,'-----------------')



for j in range(100,1000):
    # print(j)
    for i1 in range(0,6):
        for i2 in range(i1+1,6):
            for i3 in range(i2+1,6):
                count=0
                for i in range(1,10):
                    a="000000"
                    b=str(j)
                    a=repChar(a,i1,10-i)
                    a=repChar(a,i2,10-i)
                    a=repChar(a,i3,10-i)
                    cc=0
                    for z in range(0,6):
                        if z!=i1 and z!=i2 and z!=i3:
                            a=repChar(a,z,b[cc])
                            cc=cc+1
                    if(isPrime(int(a))):
                        count=count+1
                        if(count==8):
                            print(a,"done")
                    




