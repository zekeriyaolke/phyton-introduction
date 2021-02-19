minNumber=0
maxNumber=1000

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def getPrimes(minPrime, maxPrime):
    if(minPrime<minNumber or maxPrime>maxNumber):
        print("Başlangıç ve bitiş değerleri 0-1000 aralığında olmalı!")
        return ''
    primes = [i for i in range(minPrime,maxPrime) if isPrime(i)]
    return primes

def prime_first():
    return getPrimes(0, 501)


def prime_second():
    return getPrimes(501, 1000)

print(prime_first())
print(prime_second())