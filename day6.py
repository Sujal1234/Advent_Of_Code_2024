with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

guard_pos = (0, 0)
guard_dir = (-1, 0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if(not lines[i][j] in ".#"):
            guard_pos = (i, j)
            break

def rotate(direction):
    z = complex(direction[0], direction[1])
    z = z*complex(0, -1)
    return (int(z.real), int(z.imag))

def valid_ind(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def is_loop(grid, guard_pos, guard_dir):
    n, m = len(grid), len(grid[0])
    visited = set()
    next_i, next_j = add(guard_pos, guard_dir)
    while(valid_ind(next_i, next_j, n, m)):
        if(grid[next_i][next_j] == '#'):
            if((guard_pos, guard_dir) in visited):
                return True
            visited.add((guard_pos, guard_dir))
            guard_dir = rotate(guard_dir)          
            next_i, next_j = add(guard_pos, guard_dir)
        else:
            if((guard_pos, guard_dir) in visited):
                return True
            visited.add((guard_pos, guard_dir))
            guard_pos = add(guard_pos, guard_dir)
            next_i, next_j = add(guard_pos, guard_dir)
    return False

def gen_path(grid, guard_pos, guard_dir):
    n, m = len(grid), len(grid[0])
    visited = set()
    visited.add(guard_pos)
    next_i, next_j = add(guard_pos, guard_dir)
    while(valid_ind(next_i, next_j, n, m)):
        if(grid[next_i][next_j] == "#"):
            guard_dir = rotate(guard_dir)
            next_i, next_j = add(guard_pos, guard_dir)
        else:
            guard_pos = add(guard_pos, guard_dir)
            visited.add(guard_pos)
            next_i, next_j = add(guard_pos, guard_dir)
    return visited

def num_loops(grid, guard_pos, guard_dir):
    num = 0
    visited = gen_path(grid, guard_pos, guard_dir)
    for i, j in visited:
        if((i, j) == guard_pos):
            continue
        new_grid = grid.copy()
        new_grid[i] = new_grid[i][:j] + '#' + new_grid[i][j+1:]
        if(is_loop(new_grid, guard_pos, guard_dir)):
            num += 1
    return num

#For part 1:
#print(len(gen_path(lines, guard_pos, guard_dir))

#For part 2:
print(num_loops(lines, guard_pos, guard_dir))


