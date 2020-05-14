__author__  = "Bungogood"

'''
Functions libary
'''

def primes():
    arr, n = [], 1
    while True:
        c = True
        n += 1
        for p in arr:
            if n % p == 0:
                c = False
                break
            if p*p > n:
                break
        if c:
            arr.append(n)
            yield n