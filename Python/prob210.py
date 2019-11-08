import math
import numpy as np

def allPoints(n):
    base=2*n+1
    return 2*(base+1)*(n+1)/2-base



def N(r):
    count=0
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            checkForThis=abs(y)+abs(x)<=r 
            # checkForThis= not (x<=0 and y<=0)
            
            if not checkForThis:    
                count+=1
                # print([x,y])
            
    print(count)
    return (r+2)*(r/2) +  ((r+2)*(r/2)-2*r)    +    2*((r/4+1)*(r/8)-2) + (r/4+1)*(r/4)   + (r/2+2)*(r/2+1)-4 + 2*(r/4-1) +(4*(r/4-1)*(r/8))

n=8
print(allPoints(n) - (1+n/2*3+n/4+(n+1)*(n/4+1)))

#Need More work