from time import perf_counter as pc
import re
import math

def read_numbers_1(T):
    nrs = []
    for line in T:
        if (nrs_temp := re.findall(r'\d+', line)):
            nrs.append(list(map(int, nrs_temp)))
    return [row for row in zip(*nrs)]

def read_numbers_2(T):
    nrs = []
    row = []
    T = [''.join(row) for row in zip(*T)]
    for line in T:
        if (nrs_temp := re.findall(r'\d+', line)):
            row.append(int(nrs_temp[0]))
        else:
            nrs.append(row)
            row = []
    nrs.append(row) # last row - wouldnt proceeded yet
    return nrs

def read_puzzle(file):
    T = open(file).read().split("\n")
    ops = re.findall(r'[+*]', T[-1])
    nrs1 = read_numbers_1(T)
    nrs2 = read_numbers_2(T)
    return ops, nrs1, nrs2

def solve(puzzle):
    ops, nrs1, nrs2 = puzzle   
    p2 = p1 = 0  
    for (op, nr1_, nr2_) in zip(*puzzle):
        if op == "+":
            p1 += sum(nr1_)
            p2 += sum(nr2_)
        else: 
            p1 += math.prod(nr1_)
            p2 += math.prod(nr2_) 
    return p1, p2

start = pc()
puzzle = read_puzzle('d06.txt')
print("Task 1", solve(puzzle))
end = pc()
print("Time", end - start)