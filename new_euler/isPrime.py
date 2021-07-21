def isPrime(n):
    for i in range(2, int(n**(1/2)) +1):
        if(n%i == 0):
            print(i)
            return False
    return True


while(True):
    var = input("Enter a number ")
    print(isPrime(int(var)))
print(isPrime(113))