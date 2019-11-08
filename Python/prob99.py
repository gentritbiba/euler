import math
myArr=[]
with open("prob99data.txt","r") as file:
   for i in file:
       myArr.append(i[:-1].split(','))
       
maxLine,maxVal,maxIndex="",-1,0

for index,i in enumerate(myArr):
    powerNum=math.log(int(i[0]),2)
    if powerNum*int(i[1])>maxVal:
        maxVal=powerNum*int(i[1])
        maxLine=i
        maxIndex=index
print(maxLine,maxIndex+1)