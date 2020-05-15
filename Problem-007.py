from func import primes

__author__  = "Bungogood"

'''
Problem 7

10001st prime
'''

def f(x):
    p = primes()
    for _ in range(x-1):
        next(p)
    return next(p)

if __name__ == "__main__":
    print(f(10001))