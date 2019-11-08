def thysa(a,b,i):
    count=0
    for j in range(i):
        a,b=b,b*2+a
        if len(str(a+b))>len(str(b)):
            count+=1
    print(count)
    return(a,b)

thysa(1,2,1000)
