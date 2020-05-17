__author__  = "Bungogood"

'''
Problem 174

Counting the number of "hollow" square laminae 
that can form one, two, three, ... distinct arrangements
'''

def squares(lim):
    d = {}
    n = 3
    while 4*(n-1) <= lim:
        for x in range(1, (n+1)//2):
            t = 4*x*(n-x)
            if t > lim:
                break
            d[t] = d[t]+1 if t in d else 1
        n += 1
    return d

def N(n, d):
    total = 0
    for v in d.values():
        if v == n:
            total += 1
    return total

def f(b, lim):
    d = squares(lim)
    return sum(N(n, d) for n in range(1, b+1))

if __name__ == "__main__":
    print(f(10, 1000000))