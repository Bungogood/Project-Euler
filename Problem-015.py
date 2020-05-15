from func import factorial

__author__  = "Bungogood"

'''
Problem 15

Lattice paths

pascals triangle
'''

def f(x):
    return factorial(2*x)//factorial(x)**2

if __name__ == "__main__":
    print(f(20))