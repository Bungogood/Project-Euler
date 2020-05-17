__author__  = "Bungogood"

'''
Problem 67

Maximum path sum II
'''

def load(path):
    with open(path, "r") as file:
        data = list(map(lambda r: [int(c) for c in r.split(" ")], file.read().split("\n")))
    return data

def f(tri):
    for r in range(len(tri)-2, -1, -1):
        for c in range(len(tri[r])):
            tri[r][c] += tri[r+1][c] if tri[r+1][c] > tri[r+1][c+1] else tri[r+1][c+1]
    return tri[0][0]

if __name__ == "__main__":
    tri = load("files/P067-triangle.txt")
    print(f(tri))