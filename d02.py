import re
from itertools import batched
def read_puzzle(file):
    puzzle = [(int(x), int(y)) for x,y in batched(re.findall(r'[1-9][0-9]*', open(file).read()),2)]
    return puzzle

def solve(puzzle):
    re1 = re.compile(r"^([1-9][0-9]*)\1$")
    re2 = re.compile(r"^([1-9][0-9]*)\1+$")
    p2 = p1 = 0
    for (x, y) in puzzle:
        for v in range(x, y+1):
            if (re1.findall(str(v))):
                p1 += int(v)
                p2 += int(v)
            elif (re2.findall(str(v))):
                p2 += int(v)
    return p1, p2
    
puzzle = read_puzzle('d02.txt')
print("Task 1/2", solve(puzzle))