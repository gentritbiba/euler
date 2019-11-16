from myfunctions import generatePrime, eulerTotient
import time
start= time.time()

primeList = generatePrime(2,500000)

# def 
# # 





maxPhi = 0
maxN=0

# for i in range(10):
    



for n in range(2,1000000,2):
    # print(n)
    count=n
    for p in primeList:
        if p > int(n**0.5):
            break;
        if n%p == 0:
            count*= 1-1/p
            if n%(n/p) == 0 and p!=n**0.5:
                count*= 1-1/(n/p)
    phi=count
    if phi!=0 and n/phi > maxPhi:
        maxPhi=n/phi
        maxN = n
end = time.time()
print(maxN , end-start)