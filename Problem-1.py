__author__  = "Bungogood"

'''
Problem 1

Multiples of 3 and 5
'''

f = lambda: sum(x for x in range(1000) if x%3==0 or x%5==0)

if __name__ == "__main__":
    print(f())