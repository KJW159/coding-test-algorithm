# baekjoon_15685 드래곤 커브

N = int(input())
arr = [[0]*101 for _ in range(101)]
res = 0
# 0,1,2,3 방향 (x,y 반대로)
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    arr[x][y] = 1
    direction = [d]
    for __ in range(g):
        tmp_direction = direction[:]
        tmp_direction.reverse()
        for d in tmp_direction:
            direction.append((d+1)%4)

    for c in direction:
        nx = x + dx[c]
        ny = y + dy[c]
        if 0 <= nx < 101 and 0 <= ny < 101:
            arr[nx][ny] = 1
            x, y = nx, ny
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
            res += 1

print(res)






