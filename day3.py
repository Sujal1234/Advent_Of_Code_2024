with open("input.txt", 'r') as file:
    data = file.read()

def process_mul(inp, i):
    n = len(inp)
    assert inp[i:].startswith("mul(")
    i += 4
    num1 = ""
    num2 = ""
    if(i >= n):
        return None
        
    while(i < n and inp[i].isdigit()):
        num1 += inp[i]
        i += 1
    if(num1 == ""):
        return None
    # print(num1, end = " ")
        
    if(i >= n):
        return None
    if(inp[i] != ','):
        return None
    i += 1

    while(i < n and inp[i].isdigit()):
        num2 += inp[i]
        i += 1
    if(num2 == ""):
        return None
    if(i >= n):
        return None
    if(inp[i] != ')'):
        return None
    return (int(num1), int(num2))

def make_pairs(inp):
    pairs = [] #list of tuples
    i = 0
    n = len(inp)
    while(i < n):
        i = inp.find("mul(", i)
        if(i == -1):
            break

        pair = process_mul(inp, i)
        if(pair is None):
            i += 4
            continue
        pairs.append(pair)

        # length = len("mul({0},{1})".format(pair[0], pair[1]))
        i += 4
        
    return pairs

def make_pairs_new(inp):
    pairs = [] #list of tuples
    i = 0
    n = len(inp)

    enabled = True
    while(i < n):
        if(not enabled):
            #since not enabled, look for a do() first
            i = inp.find("do()", i)
            if(i == -1):
                break
            i += 4
            enabled = True
            continue

        else:
            #enabled
            x_mul = inp.find("mul(", i)
            x_dont = inp.find("don't()", i)

            # print("Mul found at {0}\nDont found at {1}".format(x_mul, x_dont))

            if(x_mul == -1):
                break
            elif(x_dont != -1 and x_dont < x_mul):
                enabled = False
                i = x_dont + 7
                continue
            else:
                #enabled
                i = x_mul

                pair = process_mul(inp, i)
                if(pair is None):
                    i += 4
                    continue
                pairs.append(pair)
                i += 4        
    return pairs

def calc_sum(pairs):
    ans = 0
    for x, y in pairs:
        ans += x*y
    return ans

#For part 1:
#p1 = make_pairs(data)

#For part 2:
p2 = make_pairs_new(data)

# print(p1)
print(p2)
# print(calc_sum(p1))
print(calc_sum(p2))