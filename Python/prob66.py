import math

# def isRoot(n):
#   if math.sqrt(n) % 1 == 0:
#     return true
#   return false

def calculateMinimalSolution(d):
  if math.sqrt(d) % 1 == 0: 
    return False
  for i in range(1,d + 100):
    x = math.sqrt(d * i*i + 1)
    if x % 1 == 0:
      return x
  print(d);
  return False

largestD = 0
largestX = 0

for i in range(7, 1001):
  x = calculateMinimalSolution(i)
  if x:
    if x > largestX:
      largestX = x
      largestD = i
      print(i, x)


print(largestD, x)