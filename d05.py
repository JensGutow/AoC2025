from time import perf_counter as pc

def read_puzzle(file):
    [goods,ingredients] =  open(file).read().split("\n\n")
    goods = [list(map( int, good.split("-"))) for good in goods.splitlines()]
    ingredients = list(map(int, ingredients.splitlines()))
    return [goods, ingredients]

def solve(puzzle):
    goods, ings = puzzle

    goods.sort()
    ings.sort()
    p1 = g = i = 0    
    while i < len(ings) and g < len(goods):
        good = goods[g]
        ing = ings[i]
        if ing < good[0]:
            i += 1
        elif ing <= good[1]:
            p1 += 1
            i += 1
        else:
            g += 1

    result = [goods.pop(0)]
    while goods:
        start = goods.pop(0)
        r = result.pop()
        if r[1] < start[0]:
            result.extend([r,start])
        else:
            result.append([r[0], max(r[1],start[1])])
    p2 = sum([r[1]-r[0]+1 for r in result])
    return p1,p2

start = pc()
puzzle = read_puzzle('d05.txt')
print("Task 1", solve(puzzle))
print("Time", pc() - start)