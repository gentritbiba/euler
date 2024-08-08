# import isPrime from myfunctions.py
from myfunctions import isPrime, generatePrime

primes = generatePrime(2,100)

def myF(n): #9
  lPrimes = filter(lambda x: x<n, primes)
  solutions = [1] + [0]*n
  for i in list(lPrimes):
    for s in range (i, n+1):
      solutions[s] += solutions[s-i]
      if(solutions[s] >= 5000):
        print(n, "done")
        return 1
  return 0
  # print(solutions);

for i in range(11,100):
  if myF(i): break
