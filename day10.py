from queue import Queue

with open("input.txt", "r") as file:
    lines = [l.strip() for l in file]
    lines = [list(map(int, l)) for l in lines]

def validInd(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#For part 1:
def bfs(grid, row, col):
    visited = [[False for i in line] for line in grid]
    q = Queue()
    q.put((row, col))
    visited[row][col] = True
    score = 0
    while(not q.empty()):
        curr_row, curr_col = q.get()
        visited[curr_row][curr_col] = True
        if(grid[curr_row][curr_col] == 9):
            score += 1
            continue
        for dr, dc in dirs:
            row_, col_ = curr_row+dr, curr_col+dc
            if not validInd(row_, col_, len(grid), len(grid[0])):
                continue
            if(visited[row_][col_]):
                continue
            if grid[row_][col_] == grid[curr_row][curr_col] + 1:
                q.put((row_, col_))
                visited[row_][col_] = True
    return score

#For part 2:
def bfs2(grid, row, col):
    num_paths = [[0 for i in line] for line in grid]
    visited = [[False for i in line] for line in grid]
    q = Queue()
    q.put((row, col))
    num_paths[row][col] = 1
    visited[row][col] = True
    rating = 0
    while(not q.empty()):
        curr_row, curr_col = q.get()
        visited[curr_row][curr_col] = True
        if(grid[curr_row][curr_col] == 9):              
            rating += num_paths[curr_row][curr_col]
            continue
        for dr, dc in dirs:
            row_, col_ = curr_row+dr, curr_col+dc
            if not validInd(row_, col_, len(grid), len(grid[0])):
                continue
            if grid[row_][col_] == grid[curr_row][curr_col] + 1:
                num_paths[row_][col_] += num_paths[curr_row][curr_col]
                if(not visited[row_][col_]):
                    q.put((row_, col_))
                    visited[row_][col_] = True
    return rating

tot = 0
for i, line in enumerate(lines):
    for j, n in enumerate(line):
        if(n == 0):
            #For part 2:
            tot += bfs2(lines, i, j)

print(tot)
