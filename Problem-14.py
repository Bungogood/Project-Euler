__author__  = "Bungogood"

'''
Problem 14

Longest Collatz sequence
'''

def g(x, d={1: 1}):
    if x in d:
        return d[x]
    else:
        tmp = g(3*x+1 if x%2 else x//2) + 1
        d[x] = tmp
        return tmp

def f(lim):
    best = 1
    largest = 1
    for n in range(1, lim):
        tmp = g(n)
        if tmp > largest:
            best = n
            largest = tmp
    return best

if __name__ == "__main__":
    print(f(1000000))