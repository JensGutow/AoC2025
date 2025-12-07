def read_puzzle(file):
    puzzle = []
    for line in open(file).read().splitlines():
        dir = line[0]
        n = int(line[1:])
        puzzle.append((dir,n))
    return puzzle

def AnzahlNulldurchGaenge(pos):
    n = (pos - (pos % 100)) // 100
    return (n)

def Correction(von, nach, dir):
    corr = 0
    if dir == "L":
        if (not von) and nach:
            corr = -1
        elif von and (not nach):
            corr = 1
    return corr

def solve(puzzle):
    pos_old = pos = 50
    p2 = p1 = 0
    for dir,n in puzzle:
        if dir == "L": n = -n
        pos += n
        if pos % 100 == 0:
            p1 += 1
        if (n := abs(AnzahlNulldurchGaenge(pos) - AnzahlNulldurchGaenge(pos_old))):
            p2 += n
        p2 += Correction(pos_old%100, pos%100, dir)
        pos_old = pos
    return p1, p2

puzzle = read_puzzle('d01.txt')
print("Task 1/2", solve(puzzle))