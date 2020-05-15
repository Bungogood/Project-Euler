__author__  = "Bungogood"

'''
Problem 16

Power digit sum
'''

def f(x):
    return sum(int(c) for c in str(2**x))

if __name__ == "__main__":
    print(f(1000))