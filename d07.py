from time import perf_counter as pc
from collections import Counter as cnt

def read_puzzle(file):
    pod = dict()
    start = None
    for y, line in enumerate(open(file).read().splitlines()):
        for x, c in enumerate(line):
            if c == 'S': start = (x,y)
            pod[(x,y)] = c
    return y+1, start, pod


def solve(puzzle):
    (y_max, start, pods) = puzzle
    (x,y) = start
    beams = {x}
    timelines = cnt([x])
    p1 = 0
    for y in range(1,y_max):
        beams2 = set()
        timelines2 = cnt()
        while beams:
            x = beams.pop()
            if pods[(x,y)] == ".": 
                beams2.add(x)
                timelines2[x] += timelines[x] 
            else:
                splitted = False
                for dx in [-1,1]:
                    if (x+dx,y) in pods: 
                        beams2.add(x+dx)
                        timelines2[x+dx] += timelines[x]
                        splitted = True
                p1 += splitted
        beams = beams2
        timelines = timelines2 
    return p1, sum(timelines.values())

start = pc()
puzzle = read_puzzle('d07.txt')
print("Task 1", solve(puzzle))
end = pc()
print("Time", end - start)