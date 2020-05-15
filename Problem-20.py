from func import factorial

__author__  = "Bungogood"

'''
Problem 19

Counting Sundays
'''

def f(x):
    return sum(int(c) for c in str(factorial(x)))

if __name__ == "__main__":
    print(f(10000))