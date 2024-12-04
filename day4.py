with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


directions = [
(-1, 0), #up
(-1, 1), #top right
(0, 1), #right
(1, 1), #bottom right
(1, 0), #down
(1, -1), #bottom left
(0, -1), #left
(-1, -1) #top left
]

def valid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dir_check(grid, i, j, dir_, word):
    dx, dy = dir_
    for ch in word:
        if((not valid(grid, i, j)) or grid[i][j] != ch):
            return False
        i += dx
        j += dy
    return True

def count_words(grid):
    num = 0
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if (ch == 'X'):
                for direction in directions:
                    if(dir_check(grid, i, j, direction, "XMAS")):
                        num += 1
    return num


def count_x(grid):
    num = 0
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if (ch == 'M'):
                diag1 = (1,1) #bottom right
                diag2 = (1,-1) #bottom left
                if(dir_check(grid, i, j, diag1, "MAS")):
                    if(dir_check(grid, i, j+2, diag2, "MAS")):
                        num += 1
                    elif(dir_check(grid, i, j+2, diag2, "SAM")):
                        num += 1

            elif (ch == 'S'):
                diag1 = (1,1) #bottom right
                diag2 = (1,-1) #bottom left
                if(dir_check(grid, i, j, diag1, "SAM")):
                    if(dir_check(grid, i, j+2, diag2, "MAS")):
                        num += 1
                    elif(dir_check(grid, i, j+2, diag2, "SAM")):
                        num += 1
    return num

#For part 1:
#print(count_words(lines))

#For part2:
print(count_x(lines))


def num_unique_words(str1):
    num = len(set(str1.split()))
    return num
