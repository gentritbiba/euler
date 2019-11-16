import math

def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True



def generatePrime(a,b):
    primeArray=[]

    starta=a
    while starta%6!=0:
        if(isPrime(starta)):
            primeArray.append(starta)
        starta+=1

    if(starta<=2 and b>=2):
        primeArray.append(2)
    for i in range(starta,b,6):
        if(isPrime(i+1)):
            primeArray.append(i+1)
        if(i%10!=0 and isPrime(i+5)):
            primeArray.append(i+5)
    if primeArray[-1]>b:
        primeArray.pop(-1)
    return primeArray

def generatePrime2(a,b):
    primeArr=[]
    if a<=2:
        primeArr.append(2)
    if a%2==0:
        a+=1
    for i in range(a,b,2):
        if(isPrime(i)):
            primeArr.append(i)
    return primeArr


def isPermutation(a,b):
    a=list(str(a))
    b=list(str(b))
    if(sum([ord(c) for c in a]) != sum([ord(c) for c in b])):
        return False
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                a[i]=''
                b[j]=''
    # print(a,b)
    return not len("".join(a))

def removeDup(x):
  return list(dict.fromkeys(x))

def tupleToList(x):
    result=""
    for i in x:
        result+=str(i)
    return result

def concatInt(a):
    result=""
    for i in a:
        result+=str(i)
    return result

def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result


def isCyclic(a,b):
    a=str(a)
    b=str(b)
    if len(a)!=4 or len(b)!=4 or a=='None' or b=='None':
        return False
    # print(a[0:2],b[2:4],a[2:4],b[0:2])
    if a[0:2]==b[2:4] or a[2:4]==b[0:2]:
        return True
    return False


def findFactors(n):
    factors=[]
    sqrt=math.sqrt(n)
    limit=int(sqrt)+1
    if sqrt % 1==0:
        factors.append(sqrt)
        limit-=1
    for i in range(2,limit):
        if n%i==0:
            factors.extend([i,n/i])
    return factors

def seriesSum(start,end,step):
    # print(closestFactor(5,2))
    return end/step*(start+end)/2

def closestFactor(b,a):
    if a%b==0:
        return a
    else:
        return int(a/b)*b


def BinarySearch(val, lys):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    if index == -1:
        return False
    return index

def isInSortedArray(n,array):
    arrayLen = len(array)
    divideThis = n
    checkThis = int(n/2)
    divideThis=int(n/2)
    while True:
        if(checkThis >= arrayLen):
            return False
        divideThis= int(divideThis/2)
        if n == array[checkThis]:
            return True
        elif n > array[checkThis]:
            checkThis+=divideThis
        elif n < array[checkThis]:
            checkThis-=divideThis
        if divideThis <= 1:
            return False



def eulerTotient(n, primeList):
    count=n
    for p in primeList:
        if p > int(n**0.5):
            break
        if n%p == 0:
            count*= 1-1/p
            if isInSortedArray(n/p,primeList) and p!=n**0.5:
                count*= 1-1/(n/p)
    return count