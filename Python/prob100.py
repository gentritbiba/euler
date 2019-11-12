import math
sqrtNum=math.sqrt(0.5)
lowerLim=11
# for i in range(lowerLim,lowerLim+1000000):
#     blueDiscs=int(i*sqrtNum)+1
#     # print((blueDiscs/i)*((blueDiscs-1)/(i-1)))
#     if (blueDiscs*(blueDiscs-1)/(i*(i-1)))==0.5:
#         print('ItWorks', blueDiscs,i)0


for a in range(-100,100):
    for b in range(-100,100):
        for c in range(-100,100):
            if 85 == a*15 + b*21 + c and 493 == a*85 + b*120 + c:
                print(a,b,c)
print("########################")
for a in range(-100,100):
    for b in range(-100,100):
        for c in range(-100,100):
            if 120 == a*15 + b*21 + c and 697 == a*85 + b*120 + c:
                print(a,b,c)

blue=15
total=21
while total<10**12:
    blue,total =3*blue + 2*total -2, 4*blue + 3 * total -3
print(blue)