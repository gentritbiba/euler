x=9

y=4

d=5

maxXD=0
maxX=0

for d in range(661, 662):
    for x in range(1, 1000 ):
        if((((x*x)/d - 1/d) ** (1/2))%1 == 0):
            if(x>maxX):
                maxX = x
                maxXD = d
            print(x,d)
print(maxX, maxXD)