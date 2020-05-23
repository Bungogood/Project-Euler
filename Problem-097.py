__author__  = "Bungogood"

'''
Problem 97

Large non-Mersenne prime
'''

def f():
    mer = 28433
    for _ in range(7830457):
        mer *= 2
        mer %= 10**10
    return mer + 1

if __name__ == "__main__":
    print(f())