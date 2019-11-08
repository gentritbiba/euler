from itertools import combinations_with_replacement 

peter = combinations_with_replacement([1,2,3,4],9)
colin = combinations_with_replacement([1,2,3,4,5,6],6)
peterArr=[]
colinArr=[]

for i in peter:
    peterArr.append(sum(i))
for i in colin:
    colinArr.append(sum(i))

peterwin=0
colinwin=0
draw=0

for j in colinArr:
    for i in peterArr:
        if i>j:
             peterwin+=1
        elif j>i:
             colinwin+=1
        elif j==i:
             draw+=1

print(round(peterwin/(peterwin+draw+colinwin),7))