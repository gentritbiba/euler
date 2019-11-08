rectCount,closestArea,result=0,9999999,0
for a in range(1,100):
    for b in range(a,100):
        rectCount=0
        for i in range(1,b+1):
                rectCount+=(i*a+i)*a/2
        if(abs(rectCount-2000000)<closestArea):
            closestArea=abs(rectCount-2000000)
            result=[a,b]
print(result[0]*result[1])


Solution took 70 miliseconds