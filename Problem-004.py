__author__  = "Bungogood"

'''
Problem 4

Largest palindrome product
'''

def f():
    largest = 0
    for a in range(100, 999):
        for b in range(999, a, -1):
            p = a*b
            s = str(p)
            if s == s[::-1]:
                if p > largest:
                    largest = p
                    break
    return largest

if __name__ == "__main__":
    print(f())