def area(x1,  y1 ,  x2 ,  y2 ,  x3 ,  y3 ): 
    return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0) 

def isInsinde(x1,y1,x2,y2,x3,y3):
    x1,y1,x2,y2,x3,y3=int(x1),int(y1),int(x2),int(y2),int(x3),int(y3)
    TotalArea=area(x1,y1,x2,y2,x3,y3)
    Area1=area(0,0,x2,y2,x3,y3)
    Area2=area(x1,y1,0,0,x3,y3)
    Area3=area(x1,y1,x2,y2,0,0)
    return TotalArea==Area1+Area2+Area3

myArr=[]
counter=0
with open("prob102data.txt","r") as file:
   for i in file:
       myArr.append(i[:-1].split(','))
       
for i in myArr:
    if isInsinde(i[0],i[1],i[2],i[3],i[4],i[5]):
        counter+=1

print(counter)