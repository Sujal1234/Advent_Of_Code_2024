with open("input.txt", "r") as file:
    nums = file.read()
    nums = list(map(int, nums.split()))

import math
from collections import defaultdict

def digs(n):
    return math.floor(math.log10(n)) + 1

steps = {0: (1,), 1:(2024,)}

def stone_trans(n):
    if n in steps:
        return steps[n]
    if(n == 0):
        steps[n] = (1, )        
    elif digs(n) % 2 == 0:
        d = int(10**(digs(n)/2))
        steps[n] = (n//d, n%d)
    else:
        steps[n] = (n*2024,)
    return steps[n]

count = defaultdict(int)
for n in nums:
    count[n] += 1

def blink(count):
    new_count = defaultdict(int)
    for n, cnt in count.items():
        new_nums = stone_trans(n)
        for num in new_nums:
            new_count[num] += cnt
    return new_count

import time

start = time.time()
count_cpy = count.copy()
for i in range(75):
    count_cpy = blink(count_cpy)
print(sum(count_cpy.values()))
print("Time:", time.time() - start)