__author__  = "Bungogood"

'''
Problem 160

Factorial trailing digits
'''

def f(x):
    fac = 1
    p = 0
    for n in range(1, x+1):
        if n % 10**p == 0:
            print(n)
            if n % 10**(p+1) == 0:
                p+=1
        fac *= n
        while fac%10==0:
            fac //= 10
        fac %= 10**5
    return fac

if __name__ == "__main__":
    print(f(1000000000000))