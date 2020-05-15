from func import primes

__author__  = "Bungogood"

'''
Problem 10

Summation of primes
'''

def f(x):
    total = 0
    for p in primes():
        if p > x:
            break
        total += p
    return total

if __name__ == "__main__":
    print(f(2000000))