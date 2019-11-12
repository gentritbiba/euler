myArr = [1,2]
i=2
for j in range(1,98):
    if j%3==0:
        myArr.append(2*i)
        i+=1
    else:
        myArr.append(1)

up=1
length=len(myArr)-1
down=myArr[length]
for i in range(0,len(myArr)-1):
    

    up=myArr[length-i-1]*down + up
    up, down = down,up

aaa=str(up + 2*down)
result=0
for i in aaa:
    result+= int(i)

print(result)
