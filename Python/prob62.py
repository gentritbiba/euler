import math
import time
from myfunctions import isPermutation

start = time.time()
numarr=[]

for i in range(1000,10000):
    numarr.append(i*i*i)

shouldContinue=True
i=1000
while shouldContinue:
    count=0
    # print(i)
    for j in range(i+1,len(numarr)):
        if isPermutation(numarr[i],numarr[j]):
            count+=1
            # print(numarr[i],numarr[j])
        if(int(math.log10(numarr[j]))>math.log10(numarr[i])):
            break
        if(count>=4):
            print(numarr[i])
            end = time.time()
            print("Solution took",end - start,"sec")
            shouldContinue=False
            break
    i+=1
        


        