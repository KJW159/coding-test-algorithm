# baekjoon_16946 벽 부수고 이동하기 4

# v1
# def dfs(s_i, s_j):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#     visited = [[0]*M for _ in range(N)]
#     stack = []
#     stack.append([s_i, s_j])
#
#     visited[s_i][s_j] = 1
#     cnt_tmp = 1
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == '0' and visited[x][y] == 0:
#                     stack.append([x, y])
#                     visited[x][y] = 1
#                     cnt_tmp += 1
#     cnt_tmp %= 10
#     return cnt_tmp
#
#
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '1':
#             move_cnt = dfs(i,j)
#             arr[i][j] = str(move_cnt)
# for i in range(N):
#     res = "".join(arr[i])
#     print(res)


#v2
# def dfs(s_i, s_j, marking):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#     stack = []
#     stack.append([s_i, s_j])
#
#     visited[s_i][s_j] = marking
#     cnt_tmp = 1
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#                 if arr[x][y] == '0' and visited[x][y] <= marking:
#                     stack.append([x, y])
#                     visited[x][y] = marking+1
#                     cnt_tmp += 1
#     cnt_tmp %= 10
#     return cnt_tmp
#
#
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# marking = -1
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '1':
#             marking += 1
#             move_cnt = dfs(i,j,marking)
#             arr[i][j] = str(move_cnt)
# for i in range(N):
#     res = "".join(arr[i])
#     print(res)



# v3
import collections

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def finding_zero(s_i, s_j, group_num):

    stack = []
    stack.append([s_i, s_j])
    visited[s_i][s_j] = group_num
    cnt_tmp = 1
    while stack:
        s_i, s_j = stack.pop()
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < N and 0 <= y < M:
                if arr[x][y] == '0' and visited[x][y] == 0:
                    stack.append([x, y])
                    visited[x][y] = group_num
                    cnt_tmp += 1
    return cnt_tmp

def moving(w_i, w_j):
    move_tmp = 1
    groups = set()
    for w in range(4):
        x = w_i + dx[w]
        y = w_j + dy[w]
        if 0 <= x < N and 0 <= y < M and arr[x][y] == '0':
            groups.add(visited[x][y])
    for group in groups:
        move_tmp += zero_group[group]
    move_tmp %= 10
    return move_tmp


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
walls = []
zero_group = collections.defaultdict(int)
group_num = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            walls.append([i,j])
        if arr[i][j] == '0' and visited[i][j] == 0:
            zero_num = finding_zero(i,j, group_num)
            zero_group[group_num] = zero_num
            group_num += 1

for w_i, w_j in walls:
    move_cnt = moving(w_i,w_j)
    arr[w_i][w_j] = str(move_cnt)

for i in range(N):
    res = "".join(arr[i])
    print(res)