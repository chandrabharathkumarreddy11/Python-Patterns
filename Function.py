##prime programs using functions
def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            #print('n is a prime')       ##printing  n is a prime number
            return True
isPrime(5)                              ####calling 
##prime in range m to m
'''
def primeNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isPrime(n):
            print(n)
primeNumbers(1,100)           ##call the main function
##n prime numbers first n 

def firstPrime(count):
    c=0
    n=2
    while True:
        if isPrime(n):
            print(n)
            c=c+1
            if c==count:
                break
        n+=1
firstPrime(10)            ## call the main function
'''
#nth prime no
def nPrime(n):
    c=0
    n=2
    while True:
        if isPrime(n):
            c=c+1
            if n==c:
                print(n)
                break
        n+=1
nPrime(10)

'''           
##Armstrong no 
def isArmstrong(n):
    t=n
    s=0
    l=len(str(t))
    while n>0:
        r=n%10
        s=r**l+s
        n//=10
    if t==s:
        return True
    else:
        return False
isArmstrong(153)
##Armstrong number in the give range
def rangeArmst(ll,ul):
    for i in range(ll,ul+1):
        if isArmstrong(i):
            print(i)
rangeArmst(20,400)
##n armstrong nos
def firstnArmstrong(count):
    c=0
    n=1
    while True:
        if isArmstrong(n):
            print(n)
            c+=1
            if c==count:
                break
        n+=1
firstnArmstrong(10)
'''

##is prime logic
def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            print(f'{n} is not a prime number')
            return False
    else:
        print(f'{n} is a Prime Number')
        return True
print(isPrime(7))


