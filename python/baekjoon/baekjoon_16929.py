# baekjoon_16929 Two Dots




# v1
# from collections import deque
#
#
# def finding_parents(parents, pre_node, next_node):
#     if parents[pre_node[0]][pre_node] != x:
#
#
#
# def bfs(i, j):
#     queue = deque()
#     queue.append([i,j])
#     visited[i][j] = 1
#     dot_color = board[i][j]
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < N and 0 <= y < M:
#
#
#
# N, M = map(int, input().split())
#
# visited = [[0]*M for _ in range(N)]
# parents = [[0]*M for _ in range(N)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# tmp = 1
# for i in range(N):
#     for j in range(M):
#         parents[i][j] = tmp
#         tmp += 1
#
# board = [list(input()) for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         if visited[i][j] == 0:
#             bfs(i,j)



# v2
# def dfs(i,j,color,cnt,si,sj):
#     global res
#     if res:
#         return
#
#     for c in range(4):
#         x = i + dx[c]
#         y = j + dy[c]
#         if 0 <= x < N and 0 <= y < M:
#             if cnt >= 4 and x == si and y == sj:
#                 res = True
#                 return
#             if visited[x][y] == 0 and board[x][y] == color:
#                 visited[x][y] = 1
#                 dfs(x,y,color,cnt+1,si,si)
#                 visited[x][y] = 0
#
#
# N, M = map(int, input().split())
#
# visited = [[0]*M for _ in range(N)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = False
# trg = False
# board = [list(input()) for _ in range(N)]
#
# for i in range(N):
#     if trg:
#         break
#     for j in range(M):
#         if visited[i][j] == 0:
#             visited[i][j] = 1
#             dfs(i,j,board[i][j],1,i,j)
#             if res:
#                 trg = True
#                 print("Yes")
#                 break
# if not res:
#     print("No")


# v3
def dfs(i,j,color,cnt,si,sj):
    global res
    if res:
        return

    for c in range(4):
        x = i + dx[c]
        y = j + dy[c]
        if 0 <= x < N and 0 <= y < M:
            if cnt >= 4 and x == si and y == sj:
                res = True
                return
            if visited[x][y] == 0 and board[x][y] == color:
                visited[x][y] = 1
                dfs(x,y,color,cnt+1,si,sj)
                visited[x][y] = 0


N, M = map(int, input().split())

visited = [[0]*M for _ in range(N)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

res = False
trg = False
board = [list(input()) for _ in range(N)]

for i in range(N):
    if trg:
        break
    for j in range(M):
        if visited[i][j] == 0:
            visited[i][j] = 1
            dfs(i,j,board[i][j],1,i,j)
            if res:
                trg = True
                break
if not res:
    print("No")
else:
    print("Yes")