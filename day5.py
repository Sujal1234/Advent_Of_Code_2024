import functools
with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

rules = {}
line_break = 0
for i, line in enumerate(lines):
    if(line == ''):
        line_break = i
        break
    n1 = int(line[:2])
    n2 = int(line[3:])
    if(n1 in rules):
        rules[n1].add(n2)
    else:
        rules[n1] = {n2}

updates = []
for i in range(line_break+1, len(lines)):
    line = lines[i]
    # print(line)
    update = line.split(',')
    update = [int(n) for n in update]
    updates.append(update)

#For part 1:
def correct(updates):
    correct_updates = [] #list of indices
    for i, update in enumerate(updates):
        valid = True
        update_dict = {}
        for j, n in enumerate(update):
            update_dict[n] = j
        for j, n in enumerate(update):
            if(not n in rules):
                continue
            rule_list = rules[n]
            for rule in rule_list:
                if(rule in update_dict):
                    if(update_dict[rule] < j):
                        valid = False
                        break
        if(valid):
            correct_updates.append(i)
    return correct_updates

def valid_middles(updates):
    mids = []
    valid_updates = correct(updates)
    for i in valid_updates:
        update = updates[i]
        n = len(update)
        assert (n % 2 == 1)
        mids.append(update[(n+1)//2 - 1])
    return mids

def middle_sum(updates):
    return sum(valid_middles(updates))
#------------------------------------------------
#For part 2:
def comp(x, y):
    if (x in rules):
        rule_set = rules[x]
        if(y in rule_set):
            return -1
        else:
            return 0
    elif (y in rules):
        rule_set = rules[y]
        if(x in rule_set):
            return 1
        else:
            return 0
    return 0

def make_valid(update):
    return sorted(update, key = functools.cmp_to_key(comp))

def incorrect(updates):
    incorrect_updates = [] #list of indices
    for i, update in enumerate(updates):
        valid = True
        update_dict = {}
        for j, n in enumerate(update):
            update_dict[n] = j
        for j, n in enumerate(update):
            if(not n in rules):
                continue
            rule_list = rules[n]
            for rule in rule_list:
                if(rule in update_dict):
                    if(update_dict[rule] < j):
                        valid = False
                        break
        if(not valid):
            incorrect_updates.append(i)
    return incorrect_updates

def invalid_middles(updates):
    mids = []
    invalid_updates = incorrect(updates)
    for i in invalid_updates:
        update = updates[i]
        update_ = make_valid(update.copy())
        n = len(update_)
        assert (n % 2 == 1)
        mids.append(update_[(n+1)//2 - 1])
    return mids

def middle_sum_invalid(updates):
    return sum(invalid_middles(updates))

#For part 1:
# print(middle_sum(updates))

#For part 2:
print(middle_sum_invalid(updates))
