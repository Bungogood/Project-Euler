__author__  = "Bungogood"

'''
Problem 160

Factorial trailing digits
'''

def f(x):
    fac = 1
    for n in range(1, x+1):
        while n%10==0:
            n //= 10
        fac *= n % 10**5
        while fac%10==0:
            fac //= 10
        fac %= 10**5
    return fac

if __name__ == "__main__":
    num = f(1000000000000)
    with open("tmp.txt", "w+") as f:
        f.write(str(num))