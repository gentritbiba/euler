# import math
# from math import gcd as bltin_gcd

# def coprime(a, b):
#     return bltin_gcd(a, b) == 1


# def diff(first, second):
#         second = set(second)
#         return [item for item in first if item not in second]

# def relatively_prime(a,b):
#     aarr=[a]
#     barr=[b]
#     alen,blen=a,b
#     counta,countb=0,0
#     sqrta=math.sqrt(a)
#     sqrtb=math.sqrt(b)
#     sqrta,sqrtb=int(sqrta),int(sqrtb)
#     for i in range(2,sqrta+1):
#         if a%i==0:
#             aarr.append(i)
#             aarr.append(a/i)
#         if b%i==0:
#             barr.append(i)
#             barr.append(b/i)
        
#     # print(aarr,barr)
#     return len(diff(aarr,barr))==len(aarr)
    
# maxrp=0
# maxi=0

# for i in range(2,1000000,4):
#     rpcount=1
#     for j in range(3,i,2):
#         if(coprime(i,j)):
#             rpcount+=1
#     irp=i/rpcount
#     # print(i,irp)
#     if irp>maxrp:
#         maxrp=irp
#         maxi=i
#         print(i, rpcount)


# print(maxi,maxrp)

# # a=['2','3','4']
# # b=['2','6']
# print(relatively_prime(25,2))
FAIL