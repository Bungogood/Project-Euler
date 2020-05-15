__author__  = "Bungogood"

'''
Problem 6

Sum square difference
'''

def f(x):
    a, b = 0, 0
    for n in range(1, x+1):
        a, b = a + 2*b*n, b+n
    return a

def g(x):
    if x == 1:
        return 0, 1
    else:
        a, b = f(x-1)
        return a + 2*b*x, b+x

if __name__ == "__main__":
    print(f(100))