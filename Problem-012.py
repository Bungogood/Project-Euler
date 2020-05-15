from func import primes

__author__  = "Bungogood"

'''
Problem 11

Summation of primes

n = number of prime factors
n! + 1 is number of factors

while prime^2 < the number:
    generate more primes
    set prime to new primes
'''

def h(t, n):
    c = 0
    while t % n == 0:
        t //= n
        c+=1
    return c

def g(t, arr, p):
    d = {}
    for a in arr:
        tmp = h(t, a)
        if tmp != 0:
            d[a] = tmp
            t //= a**tmp
    while t > 1:
        a = next(p)
        arr.append(a)
        tmp = h(t, a)
        if tmp != 0:
            d[a] = tmp
            t //= a**tmp
    prod = 1
    for e in d.values():
        prod *= e+1
    return prod

def f(x):
    p = primes()
    arr = []
    t = 1
    c = 2
    while g(t, arr, p) < x:
        t += c
        c = c+1
    return t

if __name__ == "__main__":
    print(f(500))