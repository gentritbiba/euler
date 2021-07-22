
def isPrime(n):
    if(n%2 == 0):
         return False
    for i in range(3, int(n**(1/2)) + 1, 2):
        if(n%i == 0):
            return False
    return True


    
def SieveOfEratosthenes(n):
    
    prime = [True for i in range(n+1)]
    p=2 
    while p**2 <= n:
        if(prime[p]):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    returnArr=[]
    for p in range(3, n+1):
        if(prime[p]):
            returnArr.append(p)
    return returnArr

def isConcatPrime(a,b):
    return isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a)))


def concatList(a, arr):
    cList = []
    for b in range(a+1, len(arr)):
        if(isConcatPrime(arr[a], arr[b])):
            cList.append(arr[b])
    return cList




primeList = SieveOfEratosthenes(10000)
primeLeng = len(primeList)
result = 0;
n1, n2, n3, n4, n5 = 0, 0, 0, 0, 0
for i1 in range(primeLeng):
    n1= primeList[i1]
    concatList1 = concatList(i1, primeList)
    if(concatList1):
        for i2 in range(len(concatList1)):
            n2=concatList1[i2] 
            concatList2 = concatList(i2, concatList1)
            if(concatList2):
                for i3 in range(len(concatList2)):
                    n3=concatList2[i3] 
                    concatList3 = concatList(i3, concatList2)
                    if(concatList3):
                        for i4 in range(len(concatList3)):
                            n4=concatList3[i4] 
                            concatList4 = concatList(i4, concatList3)
                            
                            if(concatList4):
                                for i5 in range(len(concatList4)):
                                    n5=concatList4[i5] 
                                    concatList5 = concatList(i5, concatList4)
                                    print(n1,n2,n3,n4,n5)
