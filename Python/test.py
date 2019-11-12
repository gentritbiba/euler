from itertools import permutations

aaa="abcde"
counter=0
for i in permutations(aaa,2):
    counter+=1

print(counter)