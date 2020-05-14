from func import primes

__author__  = "Bungogood"

'''
Problem 5

Smallest multiple

Split into prime factors
'''

def f(n=20):
    total = 1
    for p in primes():
        if p > n:
            break
        c = 1
        while p**c < n:
            c += 1
        total *= p ** (c-1)
    return total

if __name__ == "__main__":
    print(f())