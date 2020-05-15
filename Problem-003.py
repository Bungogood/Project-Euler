from func import primes

__author__  = "Bungogood"

'''
Problem 3

Largest prime factor
'''

def f():
    largest = 1
    n = 600851475143
    for p in primes():
        while n % p == 0:
            largest = p
            n /= p
        if n == 1:
            break
    return p

if __name__ == "__main__":
    print(f())