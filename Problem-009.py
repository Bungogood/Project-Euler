__author__  = "Bungogood"

'''
Problem 9

Special Pythagorean triplet
'''

def f(x):
    for c in range(x-1, x//3, -1):
        for b in range(x-c-1, (x-c)//2, -1):
            a = x - c - b
            print(c, b, a)
            if a*a + b*b == c*c:
                return a*b*c

if __name__ == "__main__":
    print(f(1000))