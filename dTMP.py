from time import perf_counter as pc

def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        puzzle.append(list(map(int, line)))
    return puzzle


def solve(puzzle, N):
    p1 = 0
    return p1

start = pc()
puzzle = read_puzzle('d03.txt')
print("Task 1", solve(puzzle))
end = pc()
print("Time", end - start)