from time import perf_counter as pc

def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        puzzle.append(list(map(int, line)))
    return puzzle

def findMax(line, start, end):
    inx_max = start
    n_max = 0
    for i, n in enumerate(range(start, len(line) - end + 1), start):
        if line[n] > n_max:
            n_max, inx_max = line[n], i
    return n_max, inx_max + 1

def solve(puzzle, N):
    voltage = 0
    for line in puzzle:
        voltage_line = start = 0
        for n in range(N, 0, -1):
            n_max, start = findMax(line, start, n)
            voltage_line = voltage_line * 10 + n_max
        voltage += voltage_line
    return voltage

start = pc()
puzzle = read_puzzle('d03.txt')
print("Task 1", solve(puzzle, 2))
print("Task 2", solve(puzzle, 12))
end = pc()
print("Time", end - start)