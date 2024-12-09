with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

#Helper functions to add/subtract coordinate vectors
def sub(t1, t2):
    return tuple(x-y for x,y in zip(t1, t2))
def add(t1, t2):
    return tuple(x+y for x,y in zip(t1, t2))

#Get a dictionary with a key = frequency and value = a list of coordinates of antennas of that frequency
def get_ants(grid):
    ants = {}
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if(ch != "." and ch != "#"):
                ants.setdefault(ch, []).append((i, j))
    return ants

ants = get_ants(lines)

def valid_ind(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def get_anti(grid, antennas):
    n, m = len(grid), len(grid[0])
    is_anti = [[False for ch in line] for line in grid]
    for stations in antennas.values():

        for i, s1 in enumerate(stations):
            for j, s2 in enumerate(stations):
                if(i == j):
                    continue
                
                diff = sub(s1, s2)
                new1 = add(diff, s1)
                new2 = sub(s2, diff)
                
                if(valid_ind(new1[0], new1[1], n, m)):
                    is_anti[new1[0]][new1[1]] = True
                    
                if(valid_ind(new2[0], new2[1], n, m)):
                    is_anti[new2[0]][new2[1]] = True
    return is_anti

#For part 2:
def get_anti_new(grid, antennas):
    n, m = len(grid), len(grid[0])
    is_anti = [[False for ch in line] for line in grid]
    for stations in antennas.values():

        for i, s1 in enumerate(stations):
            for j, s2 in enumerate(stations):
                if(i == j):
                    if(len(stations) > 1):
                        is_anti[s1[0]][s1[1]] = True
                    continue
                
                diff = sub(s1, s2)
                new1 = add(diff, s1)
                new2 = sub(s2, diff)
                
                while(valid_ind(new1[0], new1[1], n, m) or valid_ind(new2[0], new2[1], n, m)):
                    if(valid_ind(new1[0], new1[1], n, m)):
                        is_anti[new1[0]][new1[1]] = True
                        
                    if(valid_ind(new2[0], new2[1], n, m)):
                        is_anti[new2[0]][new2[1]] = True
                        
                    new1 = add(diff, new1)
                    new2 = sub(new2, diff)
    return is_anti

#For part 1:
#anti_grid = get_anti(lines, ants)

#For part 2:
anti_grid = get_anti_new(lines, ants)

tot = 0
lines_c = lines.copy()
for i, row in enumerate(anti_grid):
    for j, c in enumerate(row):
        if(c):
            lines_c[i] = lines_c[i][:j] + "#" + lines_c[i][j+1:]
            tot += 1

print(tot)
