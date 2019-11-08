from itertools import combinations


# def isValidSet(b):
#     a=len(b)
#     for gap1 in range(0,a):   
#         for g1 in range(1,a+1):   
#             for gap2 in range(0,a): 
#                 for g2 in range(1,a+1):     
#                     arr1=b[gap1:g1]
#                     arr2=b[gap2:g2]
#                     if arr1 and arr2 and arr1!=arr2:
#                         print(arr1,arr2)
#                         if sum(arr1)==sum(arr2):
#                             return False
#                         if not ((len(arr1)>len(arr2) and sum(arr1)>sum(arr2)) or (len(arr2)>len(arr1) and sum(arr1)<sum(arr2)) or len(arr1)==len(arr2)):
#                         # aaa=2
#                             return False
#     return True
# arr=[11,12,13,14,15,16,17]

# print(isValidSet(arr),sum(arr))

myArr=[20,31,37,39,40,42,45]
calcArr=[]
for j in range(1,len(myArr)):
    for i in combinations(myArr,j):
        calcArr.append(list(i))

for i in range(len(calcArr)):
    for j in range(i+1,len(calcArr)):
        if sum(calcArr[i])==sum(calcArr[j]) or not ((len(calcArr[i])>len(calcArr[j]) and sum(calcArr[i])>sum(calcArr[j])) or (len(calcArr[j])>len(calcArr[i]) and sum(calcArr[i])<sum(calcArr[j])) or len(calcArr[i])==len(calcArr[j])):
            print("False",calcArr[i],calcArr[j])
# print(calcArr)