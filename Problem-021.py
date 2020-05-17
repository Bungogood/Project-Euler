from func import primes

__author__  = "Bungogood"

'''
Problem 19

Counting Sundays
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
    return d

def perms(items, depth=0):
    if depth == len(items):
        return [1]
    out = []
    (man, exp) = items[depth]
    remaining = perms(items, depth+1)
    for e in range(exp+1):
        out += [num*man**e for num in remaining]
    return out

def amicable(n, arr, p):
    return sum(perms(list(g(n, arr, p).items())))-n

def check(n, arr, p):
    m = amicable(n, arr, p)
    return n != m and amicable(m, arr, p) == n

def f(x):
    total = 0
    arr = []
    p = primes()
    for n in range(2, x):
        if check(n, arr, p):
            total += n
    return total

if __name__ == "__main__":
    print(f(10000))