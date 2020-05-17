__author__  = "Bungogood"

'''
Problem 96

Su Doku
'''

def load(path):
    grids = []
    with open(path, "r") as file:
        data = file.read().split("\n")
        for s in range(len(data)//10):
            grid = []
            for r in range(1, 10):
                grid.append([int(c) for c in data[10*s+r]])
            grids.append(grid)
    return grids

def solve(grid, r=0, c=0):
    if c == 9:
        r, c = r+1, 0
        if r == 9:
            return True
    if grid[r][c] != 0:
        return solve(grid, r, c+1)
    sr, sc = (r//3)*3, (c//3)*3
    for v in range(1, 10):
        if valid(grid, r, c, sr, sc, v):
            grid[r][c] = v
            if solve(grid, r, c+1): 
                return True
    grid[r][c] = 0
    return False

def valid(grid, r, c, sr, sc, v):
    for i in range(9):
        if grid[r][i] == v:
            return False
        elif grid[i][c] == v:
            return False
        elif grid[sr+i//3][sc+i%3] == v:
            return False
    else:
        return True

def first3(grid):
    solve(grid)
    return grid[0][0]*100+grid[0][1]*10+grid[0][2]

def f(grids):
    return sum(first3(grid) for grid in grids)

if __name__ == "__main__":
    grids = load("files/P096-sudoku.txt")
    print(f(grids))