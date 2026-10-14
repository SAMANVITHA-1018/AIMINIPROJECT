def solve(g):
    # find the empty cell with the fewest legal digits
    best = None
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                used = {g[r][k] for k in range(9)} | {g[k][c] for k in range(9)} \
                     | {g[r//3*3 + i][c//3*3 + j] for i in range(3) for j in range(3)}
                opts = [d for d in range(1, 10) if d not in used]
                if best is None or len(opts) < len(best[2]):
                    best = (r, c, opts)
    if best is None:            # no empty cells left, so it is solved
        return True
    r, c, opts = best
    for d in opts:
        g[r][c] = d
        if solve(g):
            return True
    g[r][c] = 0                 # dead end, so undo and backtrack
    return False


# usage: 81 characters, 0 = empty
puzzle = "006209000000078000050006280000503002500020693032080150100000000003000046604905000"
grid = [[int(puzzle[r * 9 + c]) for c in range(9)] for r in range(9)]

if solve(grid):
    for row in grid:
        print(*row)
else:
    print("No solution")
