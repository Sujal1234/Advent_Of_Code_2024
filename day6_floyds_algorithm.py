with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

guard_pos = 0j
guard_dir = -1 + 0j
for i in range(len(lines)):
    for c in range(len(lines[i])):
        if(not lines[i][c] in ".#"):
            guard_pos = complex(i, c)
            break

def rotate(direction):
    return direction * (-1j)

def valid_ind(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def move(grid, pos, direc):
    if(not valid_ind(int(pos.real), int(pos.imag), len(grid), len(grid[0]))):
        return (pos, direc)
    next_pos = pos + direc
    if(not valid_ind(int(next_pos.real), int(next_pos.imag), len(grid), len(grid[0]))):
        return (next_pos, direc)
    if(grid[int(next_pos.real)][int(next_pos.imag)] == "#"):
        return (pos, rotate(direc))
    else:
        return (next_pos, direc)
    
def is_loop_2(grid, guard_pos, guard_dir):
    n, m = len(grid), len(grid[0])
    slow, fast = guard_pos, guard_pos
    slow_dir, fast_dir = guard_dir, guard_dir
    while(valid_ind(int(slow.real),int(slow.imag), n, m) and valid_ind(int(fast.real), int(fast.imag), n, m)):
        slow, slow_dir = move(grid, slow, slow_dir)
        fast, fast_dir = move(grid, fast, fast_dir)
        fast, fast_dir = move(grid, fast, fast_dir)
        if(slow == fast and slow_dir == fast_dir):
            return True

    return False

def gen_path(grid, guard_pos, guard_dir):
    n, m = len(grid), len(grid[0])
    visited = set()
    visited.add(guard_pos)
    next_pos = guard_pos + guard_dir
    while(valid_ind(next_pos.real, next_pos.imag, n, m)):
        if(grid[int(next_pos.real)][int(next_pos.imag)] == "#"):
            guard_dir = rotate(guard_dir)
            next_pos = guard_pos + guard_dir
        else:
            guard_pos = guard_pos + guard_dir
            visited.add(guard_pos)
            next_pos = guard_pos + guard_dir
    return visited

def num_loops(grid, guard_pos, guard_dir):
    num = 0
    visited = gen_path(grid, guard_pos, guard_dir)
    for pos in visited:
        if(pos == guard_pos):
            continue
        new_grid = grid.copy()
        new_grid[int(pos.real)] = new_grid[int(pos.real)][:int(pos.imag)] + '#' + new_grid[int(pos.real)][int(pos.imag)+1:]
        if(is_loop_2(new_grid, guard_pos, guard_dir)):
            num += 1
    return num

print(num_loops(lines, guard_pos, guard_dir))
