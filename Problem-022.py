__author__  = "Bungogood"

'''
Problem 22

Names scores
'''

def load(path):
    with open(path, "r") as file:
        data = file.read().replace("\"", "").split(",")
    return data

def f(names):
    names.sort()
    total = 0
    for i, name in enumerate(names):
        total += sum(ord(c)-64 for c in name)*(i+1)
    return total

if __name__ == "__main__":
    names = load("files/P022-names.txt")
    print(f(names))