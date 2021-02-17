import random

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

minPrime = 0
maxPrime = 155
matrix=[]
matrixCountX = 3
matrixCountY = 3

primes = [i for i in range(minPrime,maxPrime) if isPrime(i)]

for x in range(matrixCountX):
    a = []
    for y in range(matrixCountY):
        a.append(random.choice(primes))
    matrix.append(a)


for i in range(matrixCountX):
    for j in range(matrixCountY):
        print(matrix[i][j], end=" ")
    print()