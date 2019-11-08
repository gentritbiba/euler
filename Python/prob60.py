# import math 
# from myfunctions import generatePrime,isPrime,removeDup,tupleToList,concatInt
# from itertools import permutations 


# # class IDontKnow:
# #     def __init__(self,basePrimes,concatPrime):
# #         self.basePrimes=basePrimes
# #         self.concatPrime=concatPrime


# generatePrimes=generatePrime(1,100)

# # primeArrayCombinations= list(permutations(generatePrimes,2))
# # primeArrayCombinationsThatArePrime=[]
# # for i in primeArrayCombinations:
# #     if isPrime(int(tupleToList(i))) :
# #         primeArrayCombinationsThatArePrime.append(i)
# # print(len(primeArrayCombinationsThatArePrime))

# # newArray=[]
# # for i in primeArrayCombinationsThatArePrime:
# #     newArray.append(i[0])
# #     newArray.append(i[1])
# # newArray=removeDup(newArray)

# # count=0

# # for i in range(len(newArray)):
# #     count=0
# #     temparray=[]
# #     for j in range(i+1,len(newArray)):
# #         if isPrime(int(concatInt([i,j]))) and isPrime(int(concatInt([j,i]))):
# #             count+=1
# #             temparray.append(newArray[j])
# #     if count==5:
# #         print(i,sum(temparray))

# for i in range(len(generatePrimes)):
#     count=0
#     for j in range(i+1,len(generatePrimes)):
#         for k in range(j+1,len(generatePrimes)):
#             for l in range(k+1,len(generatePrimes)):
#                 for o in range(l+1,len(generatePrimes)):
#                     primeArrayCombinations= list(permutations([i,j,k,l,o],2))
#                     for a in primeArrayCombinations:
#                         if isPrime(int(concatInt(a))):
#                             count+=1
#     print(count)



# print(len(generatePrimes))

#FAIL