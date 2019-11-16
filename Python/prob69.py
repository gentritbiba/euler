from myfunctions import generatePrime, eulerTotient
import time
start= time.time()

primeList = generatePrime(2,500000)





maxPhi = 0
maxN=0
    



for n in range(2,1000000,2):
    # print(n)
    phi=eulerTotient(n,primeList)
    if phi!=0 and n/phi > maxPhi:
        maxPhi=n/phi
        maxN = n
end = time.time()
print(maxN , end-start)