# baekjoon_2667 단지 번호 붙이기


def dfs(i,j):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    stack = []
    stack.append([i,j])
    cnt = 1

    while stack:
        house = stack.pop()
        for c in range(4):
            x = house[0] + dx[c]
            y = house[1] + dy[c]
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] == 1 and visited[x][y] == 0:
                    stack.append([x, y])
                    visited[x][y] = 1
                    cnt += 1
                else:
                    visited[x][y] = 1
    return cnt

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
house_nums = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            house_num = dfs(i,j)
            house_nums.append(house_num)
        else:
            visited[i][j] = 1

house_nums.sort()
print(len(house_nums))
for num in house_nums:
    print(num)
