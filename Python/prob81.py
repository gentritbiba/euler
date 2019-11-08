f = open("data/matrix2.txt", "r")


a=f.read().split('\n')

matrix=[]
for i in range(len(a)):
    b=a[i].split(',')
    matrix.append([int(i) for i in b])

matlen=len(matrix)
print(matlen)

for i in range(matlen):
    for j in range (matlen):
        if i>0 and j>0:
            matrix[i][j]+=min(matrix[i-1][j],matrix[i][j-1])
        elif i>0:
            matrix[i][j]+=matrix[i-1][j]
        elif j>0:
            matrix[i][j]+=matrix[i][j-1]

print(matrix[matlen-1])