import test
from random import randint

def findSolution(matrix):
    game=matrix.copy()
    zeroCountOrg=0
    for i in range(9):
        for j in range(9):
            if game[i][j]==0:
                zeroCountOrg+=1
    zeroCount=zeroCountOrg

    counter=0
    while zeroCount>0:
        for i in range(9):
            for j in range(9):
                row=game[i]
                column=[]
                group=[]
                for c in range(9):
                    column.append(game[c][j])
                for gh in range(int(j/3)*3,int(j/3)*3+3):
                    for gv in range(int(i/3)*3,int(i/3)*3+3):
                        group.append(game[gv][gh])
                # print(group)        
                counter+=1
                # print(counter)
                possibleSolutions=[]
                if game[i][j]==0:
                    for ps in range(1,10):
                        if ps not in row and ps not in column and ps not in group:
                            possibleSolutions.append(ps)
                    if len(possibleSolutions)==1 or (counter>1000 and len(possibleSolutions)>1):
                        print(i,j,possibleSolutions[0],zeroCount ,row, column , group)
                        game[i][j]=possibleSolutions[randint(0,len(possibleSolutions)-1)]
                        zeroCount-=1
                if counter>10000:
                    return 1
                

    for i in game:
        print(i)
    # return(game[0][0]*100+game[0][1]*10+game[0][2])



print(findSolution(test.matrix))
print(findSolution(test.matrix))
print(findSolution(test.matrix))
print(findSolution(test.matrix))
# print(game[1])