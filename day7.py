
with open("test_inp.txt", 'r') as file:
    lines = [line.strip() for line in file]
with open("input.txt", 'r') as file:
    lines_real = [line.strip() for line in file]


def parse(inp):
    vals = []
    operands_list = []
    for line in inp:
        line = line.split()
        vals.append(int(line[0][:-1]))

        operands = line[1:]
        operands = [int(n) for n in operands]
        operands_list.append(operands)
    return (vals, operands_list)

vals, operands_list = parse(lines)

def maybe_valid(val, operands, prev_val, ind):
    if(len(operands) == ind):
        return val == prev_val
    if(ind == len(operands) - 1):
        return (val == operands[ind]+prev_val) or (val == operands[ind]*prev_val)
        
    ans = False
    ans = ans or maybe_valid(val, operands, prev_val + operands[ind], ind+1)
    if(ind != 0):
        ans = ans or maybe_valid(val, operands, operands[ind]*prev_val, ind+1)

    return ans

def valid_sum(vals, operands_list):
    return sum(val for i, val in enumerate(vals) if maybe_valid(val, operands_list[i], 0, 0))
        
def conc(a, b):
    return int(str(a) + str(b))

def maybe_valid_2(val, operands, prev_val, ind):
    # print(f"Val = {val}, prev_val = {prev_val}, ind = {ind}")
    if(len(operands) == ind):
        return val == prev_val
    if(ind == len(operands) - 1):
        return (val == operands[ind]+prev_val) or (val == operands[ind]*prev_val) or (val == conc(prev_val, operands[ind]))
        
    ans = False
    ans = ans or maybe_valid_2(val, operands, prev_val + operands[ind], ind+1)
    if(ind != 0):
        ans = ans or maybe_valid_2(val, operands, conc(prev_val, operands[ind]), ind+1)
    if(ind != 0):
        ans = ans or maybe_valid_2(val, operands, operands[ind]*prev_val, ind+1)

    return ans

def valid_sum_2(vals, operands_list):
    return sum(val for i, val in enumerate(vals) if maybe_valid_2(val, operands_list[i], 0, 0))
        
#For part 1:
#print(valid_sum(vals, operands_list))

#For part 2:
v, o = parse(lines_real)
print(valid_sum_2(v, o))
