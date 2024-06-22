def calculatePSQ(n, prevB, prevD = 0):
  a = prevD if prevD else int(n**(1/2))
  b = (n - a**2) / prevB
  c = int((n**(1/2) + a) / b)
  d = a - b*c
  # print("b=",b ,"c=" , c ,"d=", d)
  return (b, -d)


oddCounter = 0
for i in range(2, 10001):
  if((i**(1/2) % 1 == 0)):
    continue
  n = i
  b = 1
  d = int(n**(1/2))
  arr = [(b,d)]
  counter = 0
  while True:
    counter+=1
    b, d = calculatePSQ(n, b, d)
    if((b,d) in arr):
      if(counter % 2 == 1):
        oddCounter += 1
      break 

print(oddCounter)