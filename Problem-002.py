__author__  = "Bungogood"

'''
Problem 2

Even Fibonacci numbers
'''

def f():
    total, a, b = 0, 1, 2
    while a < 4000000:
        if b%2 == 0:
            total += b
        a, b = b, b+a
    return total

if __name__ == "__main__":
    print(f())