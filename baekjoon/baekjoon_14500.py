# baekjoon_14500 테트로미노
# v1
# figures = [[(0,1),(1,1),(1,0)],
#            [(1,0),(2,0),(3,0)],
#            [(0,1),(0,2),(0,3)],
#            [(0,1),(-1,1),(0,2)],
#            [(1,0),(1,1),(2,0)],
#            [(0,1),(0,2),(1,1)],
#            [(1,0),(1,-1),(2,0)],
#            [(1,0),(1,1),(2,1)],
#            [(0,1),(-1,1),(-1,2)],
#            [(1,0),(1,-1),(2,-1)],
#            [(0,1),(1,1),(1,2)],
#            [(1,0),(2,0),(2,1)],
#            [(1,0),(0,1),(0,2)],
#            [(0,1),(1,1),(2,1)],
#            [(1,0),(1,-1),(1,-2)],
#            [(1,0),(2,0),(2,-1)],
#            [(0,1),(0,2),(1,2)],
#            [(0,1),(1,0),(2,0)],
#            [(1,0),(1,1),(1,2)]
#            ]
#
# N,M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# for i in range(N):
#     for j in range(M):
#         for k in range(19):
#             tmp = 0
#             try:
#                 tmp += arr[i][j]
#                 for f in range(3):
#                     x = i + figures[k][f][0]
#                     y = j + figures[k][f][1]
#                     tmp += arr[x][y]
#                 if tmp > res:
#                     res = tmp
#             except:
#                 continue
# print(res)

# v2
# figures = [[(0,1),(1,1),(1,0)],
#            [(1,0),(2,0),(3,0)],
#            [(0,1),(0,2),(0,3)],
#            [(0,1),(-1,1),(0,2)],
#            [(1,0),(1,1),(2,0)],
#            [(0,1),(0,2),(1,1)],
#            [(1,0),(1,-1),(2,0)],
#            [(1,0),(1,1),(2,1)],
#            [(0,1),(-1,1),(-1,2)],
#            [(1,0),(1,-1),(2,-1)],
#            [(0,1),(1,1),(1,2)],
#            [(1,0),(2,0),(2,1)],
#            [(1,0),(0,1),(0,2)],
#            [(0,1),(1,1),(2,1)],
#            [(1,0),(1,-1),(1,-2)],
#            [(1,0),(2,0),(2,-1)],
#            [(0,1),(0,2),(1,2)],
#            [(0,1),(1,0),(2,0)],
#            [(1,0),(1,1),(1,2)]
#            ]
#
# N,M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# res = 0
# for i in range(N):
#     for j in range(M):
#         for k in range(19):
#             tmp = 0
#             tmp += arr[i][j]
#             for f in range(3):
#                 x = i + figures[k][f][0]
#                 y = j + figures[k][f][1]
#                 if 0 <= x < N and 0 <= y < M:
#                     tmp += arr[x][y]
#                 else:
#                     continue
#             if tmp > res:
#                 res = tmp
# print(res)

# v3
def dfs(i,j,cnt,num):
    global res
    if cnt == 4:
        res = max(res, num)
        return
    for c in range(4):
        x = i + dx[c]
        y = j + dy[c]
        if 0 <= x < N and 0 <= y < M and visited[x][y] == 0:
            visited[x][y] = 1
            dfs(x, y, cnt+1, num+arr[x][y])
            visited[x][y] = 0

def wo_shape(i,j):
    global res

    for k in range(4):
        cnt = 1
        num = arr[i][j]
        for f in range(3):
            x = i + figures[k][f][0]
            y = j + figures[k][f][1]
            if 0 <= x < N and 0 <= y < M:
                num += arr[x][y]
                cnt += 1
            else:
                break
        if cnt == 4:
            res = max(res, num)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

figures = [[(0,1),(0,2),(1,1)],
           [(1,0),(2,0),(1,1)],
           [(0,1),(0,2),(-1,1)],
           [(1,0),(2,0),(1,-1)]
           ]
res = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,1,arr[i][j])
        wo_shape(i,j)
        visited[i][j] = 0
print(res)