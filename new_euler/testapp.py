
def isPrime(n):
    if(n%2 == 0):
         return False
    for i in range(3, int(n**(1/2)) + 1, 2):
        if(n%i == 0):
            # print(i)
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

primeList = SieveOfEratosthenes(10000)
primeLeng = len(primeList)
result = 0;

# The smallest number has to be lower than 100
def checkAndReturn(arr, limitNeeded):
    arrLeng = len(arr)
    tempList = []
    for j in range(i+1, arrLeng):
        if(isConcatPrime(arr[i], arr[j])):
            tempList.append(arr[j])
    if(len(tempList) >= limitNeeded):
         return tempList
    print(tempList)
    return []

tempList = []

for i in range(4,5):
#     newList = checkAndReturn(primeList, 5)
    
#     newList = checkAndReturn(newList, 4)
#     newList = checkAndReturn(newList, 3)
    # print(primeList[i], len(newList))
    for j in range(i+1, primeLeng):
        if(isConcatPrime(primeList[4], primeList[j])):
            tempList.append(primeList[j])
    print(primeList[i])
for i in range(len(tempList)):
    tempList2 = []
    for j in range(i + 1, len(tempList)):
        if(isConcatPrime(tempList[i], tempList[j])):
            tempList2.append(tempList[j])
    if(len(tempList2) >=4 ):
        print(tempList[i], len(tempList2))
# print(tempList2)

# print(result)
print(result)

# print(isConcatPrime(7,11))

# print(len(SieveOfEratosthenes(10000)))
# print(prime)