
from myfunctions import removeDup

def retK(n):
    startArray=[]
    for i in range(n):
        startArray.append(1)
    
    startArray2=startArray.copy()
    changeThis=n-1
    maxlimit=n
    sumArray=0
    while True:
        
        n2=1

        sumArray=startArray2[n-2]+startArray2[n-1]+startArray2[n-3]+startArray2[n-4]+startArray2[n-5]+n-5
        numOfMult=n-6
        n2=startArray2[n-2]*startArray2[n-1]*startArray2[n-5]*startArray2[n-4]*startArray2[n-3]
        
        # print(n2,sumArray,startArray2)
        if n2==sumArray:
            # print(n2,sumArray)
            return sumArray

        if startArray2[changeThis] <= maxlimit :
            startArray2[changeThis]+=1
            # print('caseA')

            
        else:
            # print('caseB')
            changeThis-=1
        if changeThis < n-4:
            startArray2=startArray.copy()
            maxlimit-=1
            changeThis=n-1
            # print('caseC',startArray2)
        if maxlimit==0:
            print('failure')
            break
        sumArray=sum(startArray2)

finalArray=[]
for i in range(13,12001):
    print(i)
    finalArray.append(retK(i))
finalArray=removeDup(finalArray)
print(sum(finalArray))