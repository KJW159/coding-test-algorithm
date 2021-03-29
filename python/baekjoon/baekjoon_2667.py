# baekjoon_2667 단지번호붙이기

def dfs(i,j):
    stack = [[i,j]]
    arr[i][j] = 2
    cnt_tmp = 1
    while stack:
        s_i, s_j = stack.pop()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0<=x<N and 0<=y<N:
                if arr[x][y] == 1:
                    stack.append([x,y])
                    arr[x][y] = 2
                    cnt_tmp += 1
    return cnt_tmp

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
res_num = 0
res_nums = []

dx = [0,-1,0,1]
dy = [-1,0,1,0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            res_nums.append(dfs(i,j))
            res_num += 1
res_nums.sort()
print(res_num)
for k in range(res_num):
    print(res_nums[k])