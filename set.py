#Built-in-methods of set
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
def rev(n):
    revnum=0
    while n>0:
        r=n%10
        n=n//10
        revnum=revnum*10+r
        return revnum
def isEmirp(n):
    if isPrime(n) and isPrime(rev(n)) and n!=rev(n):
        return True
    
    else:
        return False
    
print(isEmirp(17))



S='Narayana'
S=S.lower().swapcase()
print(S)


s='PROGRAM'
for i in range(1,len(s)+1):

            if i<=len(s)//2+1:
                print(' '*((len(s)*2)-(i+1)),s[len(s)//2:(len(s)//2)+i:])
        #     else:
        #         print(' '*(len(s)-i),s[5-i])
        # print()

''' SELECT CASE
 WHEN ROWNUM<=7 THEN LOWER(ENAME) ELSE UPPER(ENAME) END FROM EMP;'''




##Spiral Pattern

def print_spiral(n):
    # Create an n x n matrix filled with zeros
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    
    # Initialize the boundaries
    left, right = 0, n-1
    top, bottom = 0, n-1
    
    # Initialize the starting number
    num = 1
    
    while left <= right and top <= bottom:
        # Fill the top row
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1
        
        # Fill the right column
        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1
        
        # Fill the bottom row
        for i in range(right, left - 1, -1):
            spiral[bottom][i] = num
            num += 1
        bottom -= 1
        
        # Fill the left column
        for i in range(bottom, top - 1, -1):
            spiral[i][left] = num
            num += 1
        left += 1
    
    # Print the spiral matrix
    for row in spiral:
        print(" ".join(str(x).rjust(3, " ") for x in row))

# Example usage
n = 7
print_spiral(n)

