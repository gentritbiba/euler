from myfunctions import isCyclic, removeDup

def finalCheck(a):
    isTrue1=False
    isTrue2=False
    for i in range(len(a)-1):
        if str(a[len(a)-1])[2:4]==str(a[i])[0:2]:
            isTrue1=True
    for i in range(len(a)-1):
        if str(a[len(a)-1])[0:2]==str(a[i])[2:4]:
            isTrue2=True
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if str(a[i])[0:2]==str(a[j])[0:2] or str(a[i])[2:4]==str(a[j])[2:4]:
                # print(a[i],a[j])
                return False
    return isTrue1 and isTrue2


triangle,square,pentagonal,hexagonal,heptagonal,octagonal,triangleFriends,triangleFriends2,triangleFriends3,triangleFriends4,triangleFriends5=[],[],[],[],[],[],[],[],[],[],[]

tempVal=-1
for i in range(1,141):
    tempVal=int(i*(i+1)/2)
    triangle.append(tempVal) if len(str(tempVal))==4 else triangle.append(0) 

    tempVal=int(i*i)
    square.append(tempVal) if len(str(tempVal))==4 else square.append(0) 

    tempVal=int(i*(3*i-1)/2)
    pentagonal.append(tempVal) if len(str(tempVal))==4 else pentagonal.append(0) 

    tempVal=int(i*(2*i-1))
    hexagonal.append(tempVal) if len(str(tempVal))==4 else hexagonal.append(0) 

    tempVal=int(i*(5*i-3)/2)
    heptagonal.append(tempVal) if len(str(tempVal))==4 else heptagonal.append(0) 

    tempVal=int(i*(3*i-2))
    octagonal.append(tempVal) if len(str(tempVal))==4 else octagonal.append(0) 

for a in triangle:
    for b in square:
        if isCyclic(a,b):
            triangleFriends.append([a,b])
for index,a in enumerate(triangleFriends):
    for b in pentagonal:
        for i in a:
            if isCyclic(i,b):
                tempArray=a.copy()
                tempArray.extend([b])
                triangleFriends2.append(tempArray)
                break
for index,a in enumerate(triangleFriends2):
    for b in hexagonal:
        for i in a:
            if isCyclic(i,b):
                tempArray=a.copy()
                tempArray.extend([b])
                triangleFriends3.append(tempArray)
                break
for index,a in enumerate(triangleFriends3):
    for b in heptagonal:
        for i in a:
            if isCyclic(i,b):
                tempArray=a.copy()
                tempArray.extend([b])
                triangleFriends4.append(tempArray)
                break
for index,a in enumerate(triangleFriends4):
    for b in octagonal:
        for i in a:
            if isCyclic(i,b):
                tempArray=a.copy()
                tempArray.extend([b])
                triangleFriends5.append(tempArray)
                break
        

for i in triangleFriends5:
    if finalCheck(i):
        print(i,sum(i))

            

