def findSolutionForD(d):
  y = 0;
  while True:
    y+=1
    x = (1+d*y**2)**(1/2)
    if(x % 1 == 0):
      print(x, y, d)
      return(x)
      break
  return 0
    
# maxX=0
# maxD=0
# for d in range(3,1001):
#   x=0
#   if d**(1/2) % 1 == 0:
#     continue
#   x = findSolutionForD(d)
#   if(d == 661):
#     print(x)
#   # print(maxX, maxD)
#   if x>maxX: 
#     maxX = x
#     maxD = d


print(findSolutionForD(661)>findSolutionForD(662))
# findSolutionForD(13)

# x=9

# y=4

# d=5

# maxXD=0
# maxX=0

# for d in range(661, 662):
#     for x in range(1, 1000 ):
#         if((((x*x)/d - 1/d) ** (1/2))%1 == 0):
#             if(x>maxX):
#                 maxX = x
#                 maxXD = d
#             print(x,d)
# print(maxX, maxXD)