from collections import Counter, defaultdict
from time import perf_counter as pc

def read_puzzle(file):
    puzzle = {(x,y) for y, line in enumerate(open(file).read().splitlines()) for x, c in enumerate(line) if c == '@'}
    return puzzle

def nbs(x, y, p):
    n = 0
    for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]:
        if (x + dx, y + dy) in p:
            n += 1
    return n < 4

def solve(puzzle):
   goodPapers = {k for k in puzzle if nbs(*k, puzzle)}
   p1 = len(goodPapers)
   p2 = 0
   while goodPapers:
       p2 += len(goodPapers)
       puzzle = puzzle - goodPapers
       goodPapers = {k for k in puzzle if nbs(*k, puzzle)}
   return p1, p2


start = pc()
puzzle = read_puzzle('d04.txt')
print("Task 1", solve(puzzle))
end = pc()
print("Time", end - start)
