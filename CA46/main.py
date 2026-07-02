N, M = map(int, input().split())

mapgrid = []
for i in range(N):
    mapgrid.append(list(input().strip()))

goldgrid = []
for i in range(N):
    goldgrid.append(list(map(int,input().split())))

grid = []
for i in range(N):
    grid.append([-1] * M)

if mapgrid[0][0] == '#':
    print(-1)
    exit()
else:
    grid[0][0] = goldgrid[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue

        if mapgrid[i][j] == '#':
            continue

        above = -1
        left = -1

        if i>0:
            above = grid[i-1][j]

        if j > 0:
            left = grid[i][j-1]

        maxamount = max(above,left)

        if maxamount != -1:
            grid[i][j] = goldgrid[i][j] + maxamount

print(grid[N-1][M-1])