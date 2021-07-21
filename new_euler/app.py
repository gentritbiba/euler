
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
    allList = []
    for i in range(min(100, len(arr))):
        print(i)
        arrLeng = len(arr)
        tempList = []
        for j in range(i+1, arrLeng):
            if(isConcatPrime(arr[i], arr[j])):
                tempList.append(arr[j])
        if(len(tempList) >= limitNeeded):
            print(arr[i], tempList)
            allList.append(tempList)
        # print(tempList)
    return allList


newList = checkAndReturn(primeList, 5)
# print(newList)
# newList = checkAndReturn(0, newList, 4)
# newList = checkAndReturn(0, newList, 3)

# print(primeList[i], len(newList))
# tempList = []
# for j in range(i+1, primeLeng):
#     if(isConcatPrime(primeList[i], primeList[j])):
#         tempList.append(primeList[j])
# print(len(tempList))
# if(len(tempList) > 5):
#      result = result + 1 

# print(result)
print("Done")

# print(isConcatPrime(7,11))

# print(len(SieveOfEratosthenes(10000)))
# print(prime)