import time
with open('prob96data.txt','r') as theFile:
    matrix=[]
    tempArr=[]
    counter=0
    for index,i in enumerate(theFile):
        if index%10!=0:
            counter+=1
            tempArr.append(list(map(int,list(i[:9]))))
            if index!=0 and counter==9:
                counter=0
                matrix.append(tempArr)
                tempArr=[]
start = time.time()

def copyArray(array):
    newArray=[]

    for i in range(len(array)):
        testArray=[]
        for j in range(len(array[i])):
            testArray.append(array[i][j])
        newArray.append(testArray)
            
    return newArray


def findSolution(matrix):
    game=copyArray(matrix)
    zeroCountOrg=0

    for i in range(9):
        for j in range(9):
            if game[i][j]==0:
                zeroCountOrg+=1

    zeroCount=zeroCountOrg
    shouldContinue=True
    counter=0
    while counter<=81*zeroCountOrg:
        for i in range(9):
            for j in range(9):
                counter+=1
                row=game[i]
                column=[]
                group=[]
                for c in range(9):
                    column.append(game[c][j])

                for gh in range(int(j/3)*3,int(j/3)*3+3):
                    for gv in range(int(i/3)*3,int(i/3)*3+3):
                        group.append(game[gv][gh])

                possibleSolutions=[]
                if game[i][j]==0:
                    for ps in range(1,10):
                        if ps not in row and ps not in column and ps not in group:
                            possibleSolutions.append(ps)

                    if len(possibleSolutions)<1:
                        return None

                    if len(possibleSolutions)==1:
                        game[i][j]=possibleSolutions[0]
                        zeroCount-=1
                        if zeroCount==0:
                            return game

                    elif (len(possibleSolutions)==2 and counter>=81*zeroCount):
                        # print(len(possibleSolutions))
                        for aa in possibleSolutions:
                            game[i][j]=aa
                            # print(game[0])
                            theGame=findSolution(copyArray(game))
                            if theGame:
                                return theGame
            
result=0
for index,i in enumerate(matrix):
    print(index)
    tR=findSolution(copyArray(i))[0]
    result+=tR[0]*100+tR[1]*10+tR[2]
end = time.time()

print(result,end-start)

# print(game[1])