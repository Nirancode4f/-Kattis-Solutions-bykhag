def check_coverage(grid, width, height, i, j):
    if i - 1 >= 0:
        if grid[i - 1][j] == "E":
            return True
    if j - 1 >= 0:
        if grid[i][j - 1] == "E":
            return True
    return False

height, width = map(int, input().split())

grid = []

for i in range(height):
    grid.append(list(input()))


for i in range(height):
    prev = []
    for j in range(width):
        if grid[i][j] == "#":

            if len(prev) != 0:
                grid[prev[0]][prev[1]] = "E"
                prev = []
            continue

        if check_coverage(grid, width, height, i, j):
            if len(prev) != 0:
                grid[prev[0]][prev[1]] = "E"
                prev = []
            continue
        else:

            if len(prev) == 0:
                prev = [i, j]
                continue
            else:
                grid[i][j] = "E"
                prev = []
    if len(prev) != 0:
        grid[prev[0]][prev[1]] = "E"

for row in grid:
    print("".join(row))
