# baekjoon_3197 백조의 호수


# v1
# import math
# from collections import deque
#
# def bfs():
#     queue = deque()
#     for i in range(1, 3):
#         s_i, s_j = swans[i]
#         queue.append([s_i, s_j, i])
#         visited[s_i][s_j][0] = 0
#         visited[s_i][s_j][1] = i
#
#     while queue:
#         s_i, s_j, s_num = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] == 0 or visited[x][y][1] == s_num:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y,s_num])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         visited[x][y][1] = s_num
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y,s_num])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = s_num
#                 if visited[x][y][1] != 0 and visited[x][y][1] != s_num:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#
# INF = math.inf
# R, C = map(int, input().split())
# lake = [list(input()) for _ in range(R)]
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# # 백조 좌표, 인덱스로 구분, 0은 인덱스 1,2로 맞춰줄려고 넣음.
# swans = [0]
# res = 0
# for i in range(R):
#     for j in range(C):
#         if lake[i][j] == "L":
#             swans.append([i,j])
#
# res = bfs()
# print(res)



# v2
# import math
# from collections import deque
#
#
# def dfs(s_i,s_j, s_num):
#     stack = [[s_i, s_j]]
#     start_pos = []
#     visited[s_i][s_j][0] = 0
#     visited[s_i][s_j][1] = s_num
#     start_pos.append([s_i, s_j, s_num])
#
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     stack.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = s_num
#                     start_pos.append([x,y, s_num])
#     return start_pos
#
#
# def bfs(queue):
#
#     while queue:
#         s_i, s_j, s_num = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 if visited[x][y][1] == 0 or visited[x][y][1] == s_num:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y,s_num])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         visited[x][y][1] = s_num
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y,s_num])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = s_num
#                 if visited[x][y][1] != 0 and visited[x][y][1] != s_num:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# lake = [list(input()) for _ in range(R)]
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# swans = [0]
# res = 0
# num = 0
# queue = deque()
# for i in range(R):
#     for j in range(C):
#         if lake[i][j] == "L":
#             num += 1
#             swans.append([i,j])
#             queue.extend(dfs(i,j,num))
#
# res = bfs(queue)
# print(res)


# v3
# import math
# from collections import deque
#
#
# def dfs(s_i,s_j, s_num):
#     stack = [[s_i, s_j]]
#     start_pos = []
#     visited[s_i][s_j][0] = 0
#     visited[s_i][s_j][1] = s_num
#     start_pos.append([s_i, s_j])
#
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     stack.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = s_num
#                     start_pos.append([x,y])
#     return start_pos
#
#
# def bfs(queue):
#
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] == 0 or visited[x][y][1] == visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         visited[x][y][1] = visited[s_i][s_j][1]
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#                 if visited[x][y][1] != 0 and visited[x][y][1] != visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# lake = [list(input()) for _ in range(R)]
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# # 백조 좌표, 인덱스로 구분, 0은 인덱스 1,2로 맞춰줄려고 넣음.
# res = 0
# num = 0
# queue = deque()
# for i in range(R):
#     for j in range(C):
#         if lake[i][j] == "L":
#             num += 1
#             queue.extend(dfs(i,j,num))
#
# res = bfs(queue)
# print(res)


# v4
# import math
# from collections import deque
#
#
# def dfs(s_i,s_j, s_num):
#     stack = [[s_i, s_j]]
#     start_pos = []
#     visited[s_i][s_j][0] = 0
#     visited[s_i][s_j][1] = s_num
#     start_pos.append([s_i, s_j])
#
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     stack.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = s_num
#                     start_pos.append([x,y])
#     return start_pos
#
#
# def bfs(queue):
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] == 0 or visited[x][y][1] == visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         if visited[x][y][1] == 0:
#                             visited[x][y][1] = visited[s_i][s_j][1]
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#                 if visited[x][y][1] != 0 and visited[x][y][1] != visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# lake = [list(input()) for _ in range(R)]
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# res = 0
# num = 0
# queue = deque()
# for i in range(R):
#     for j in range(C):
#         if lake[i][j] == "L":
#             num += 1
#             queue.extend(dfs(i,j,num))
#
# res = bfs(queue)
# print(res)


#v5
# import math
# from collections import deque
#
#
# def bfs2(swan):
#     s_i, s_j, s_num = swan
#     queue2 = deque()
#     queue2.append([s_i, s_j])
#     start_pos = []
#     visited[s_i][s_j][0] = 0
#     visited[s_i][s_j][1] = s_num
#     start_pos.append([s_i, s_j])
#
#     while queue2:
#         s_i, s_j = queue2.popleft()
#         trg = False
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     queue2.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = s_num
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == "X" and not trg:
#                 trg = True
#         if trg:
#             start_pos.append([s_i, s_j])
#     return start_pos
#
#
# def bfs(queue):
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] != 0 and visited[x][y][1] != visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#                 if visited[x][y][1] == 0 or visited[x][y][1] == visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         if visited[x][y][1] == 0:
#                             visited[x][y][1] = visited[s_i][s_j][1]
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# lake = []
# num = 0
# swans = []
# for i in range(R):
#     lake_tmp = list(input())
#     lake.append(lake_tmp)
#     for j in range(C):
#         if lake_tmp[j] == "L":
#             num += 1
#             swans.append([i,j,num])
#
#
# num = 0
# queue = deque()
# for swan in swans:
#     queue.extend(bfs2(swan))
#
# res = bfs(queue)
# print(res)


# v6
# import math
# from collections import deque
#
#
# def bfs2(swans):
#     queue2 = deque()
#     start_pos = []
#
#     for swan in swans:
#         s_i, s_j, s_num = swan
#         queue2.append([s_i, s_j])
#         visited[s_i][s_j][0] = 0
#         visited[s_i][s_j][1] = s_num
#         start_pos.append([s_i, s_j])
#
#     while queue2:
#         s_i, s_j = queue2.popleft()
#         trg = False
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     queue2.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = visited[s_i][s_j][1]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == "X" and not trg:
#                 trg = True
#         if trg:
#             start_pos.append([s_i, s_j])
#     return start_pos
#
#
# def bfs(queue):
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] != 0 and visited[x][y][1] != visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#                 if visited[x][y][1] == 0 or visited[x][y][1] == visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         if visited[x][y][1] == 0:
#                             visited[x][y][1] = visited[s_i][s_j][1]
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# lake = []
# num = 0
# swans = []
# for i in range(R):
#     lake_tmp = list(input())
#     lake.append(lake_tmp)
#     for j in range(C):
#         if lake_tmp[j] == "L":
#             num += 1
#             swans.append([i,j,num])
#
#
# num = 0
# queue = deque()
# queue.extend(bfs2(swans))
# res = bfs(queue)
# print(res)

# v7
# import math
# from collections import deque
# def bfs2(swan):
#     s_i, s_j, s_num = swan
#     queue2 = deque()
#     queue2.append([s_i, s_j])
#     start_pos = []
#     visited[s_i][s_j][0] = 0
#     visited[s_i][s_j][1] = s_num
#     start_pos.append([s_i, s_j])
#
#     while queue2:
#         s_i, s_j = queue2.popleft()
#         trg = False
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == ".":
#                 if visited[x][y][0] != 0 and visited[x][y][1] == 0:
#                     queue2.append([x,y])
#                     visited[x][y][0] = 0
#                     visited[x][y][1] = s_num
#             if 0 <= x < R and 0 <= y < C and lake[x][y] == "X" and not trg:
#                 trg = True
#         if trg:
#             start_pos.append([s_i, s_j])
#     return start_pos
#
#
# def bfs(queue):
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 # 0이거나 나랑 같은 경우 -> 이동 여부 파악해서 이동.
#                 # 번호가 다른 경우 -> 끝남.
#                 if visited[x][y][1] != 0 and visited[x][y][1] != visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0]:
#                         return visited[x][y][0]
#                     else:
#                         return visited[s_i][s_j][0]
#                 if visited[x][y][1] == 0 or visited[x][y][1] == visited[s_i][s_j][1]:
#                     if visited[x][y][0] > visited[s_i][s_j][0] and lake[x][y] == ".":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]
#                         if visited[x][y][1] == 0:
#                             visited[x][y][1] = visited[s_i][s_j][1]
#                     if visited[x][y][0] > visited[s_i][s_j][0]+1 and lake[x][y] == "X":
#                         queue.append([x,y])
#                         visited[x][y][0] = visited[s_i][s_j][0]+1
#                         visited[x][y][1] = visited[s_i][s_j][1]
#
#
# INF = math.inf
# R, C = map(int, input().split())
# visited = [[[INF,0] for __ in range(C)] for _ in range(R)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# lake = []
# num = 0
# swans = []
# for i in range(R):
#     lake_tmp = list(input())
#     lake.append(lake_tmp)
#     for j in range(C):
#         if lake_tmp[j] == "L":
#             num += 1
#             swans.append([i,j,num])
#
#
# queue = deque()
# for swan in swans:
#     queue.extend(bfs2(swan))
#
# res = bfs(queue)
# print(res)
# print(visited)




# v8
# from collections import deque
#
# def moving_swan():
#     while q_s:
#         s_i, s_j = q_s.popleft()
#         if s_i == swans[1][0] and s_j == swans[1][1]:
#             return 1
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 if visited_swan[x][y] == 0:
#                     if lake[x][y] == '.':
#                         q_s.append([x, y])
#                     elif lake[x][y] == 'X':
#                         # 다음날에 녹을 예정이므로, 이동할 수 있으니 임시에 넣어줌.
#                         q_st.append([x, y])
#                     visited_swan[x][y] = 1
#
#     return 0
#
#
# def melting_ice():
#     while q_w:
#         s_i, s_j = q_w.popleft()
#         # 전날에 녹을 예정이였던 빙판 녹이기.
#         if lake[s_i][s_j] == 'X':
#             lake[s_i][s_j] = '.'
#
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < R and 0 <= y < C:
#                 if visited_water[x][y] == 0:
#                     if lake[x][y] == 'X':
#                         # 다음날 녹은 빙판 좌표 큐에 저장.
#                         q_wt.append([x, y])
#                     else:
#                         q_w.append([x, y])
#                     # 이번에 이동하든 다음날 녹을 예정이든 큐에 들어가니 방문 처리해줌.
#                     visited_water[x][y] = 1
#
#
# R, C = map(int, input().split())
# visited_water = [[0]*C for _ in range(R)]
# visited_swan = [[0]*C for _ in range(R)]
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# lake = []
# swans = []
#
# # q_w는 물, q_s는 백조, t는 tmp
# q_w, q_s, q_wt, q_st = deque(),deque(),deque(),deque()
# res = 0
# for i in range(R):
#     lake_tmp = list(input())
#     lake.append(lake_tmp)
#     for j in range(C):
#         if lake_tmp[j] == 'L':
#             swans.append([i,j])
#             visited_water[i][j] = 1
#         elif lake_tmp[j] == '.':
#             q_w.append([i,j])
#             visited_water[i][j] = 1
#
#
# q_s.append(swans[0])
# visited_swan[swans[0][0]][swans[0][1]] = 1
# for swan in swans:
#     lake[swan[0]][swan[1]] = '.'
#
# while True:
#     melting_ice()
#     if moving_swan():
#         break
#     q_s, q_w = q_st, q_wt
#     q_st, q_wt = deque(), deque()
#     res += 1
#
# print(res)

# v9
from collections import deque

def moving_swan():
    while q_s:
        s_i, s_j = q_s.popleft()
        if s_i == swans[1][0] and s_j == swans[1][1]:
            return 1
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < R and 0 <= y < C:
                if visited_swan[x][y] == 0:
                    if lake[x][y] == '.':
                        q_s.append([x, y])
                    elif lake[x][y] == 'X':
                        # 다음날에 녹을 예정이므로, 이동할 수 있으니 임시에 넣어줌.
                        q_st.append([x, y])
                    visited_swan[x][y] = 1

    return 0


def melting_ice():
    while q_w:
        s_i, s_j = q_w.popleft()
        # 전날에 녹을 예정이였던 빙판 녹이기.
        if lake[s_i][s_j] == 'X':
            lake[s_i][s_j] = '.'

        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < R and 0 <= y < C:
                if visited_water[x][y] == 0:
                    if lake[x][y] == 'X':
                        # 다음날 녹은 빙판 좌표 큐에 저장.
                        q_wt.append([x, y])
                    else:
                        q_w.append([x, y])
                    # 이번에 이동하든 다음날 녹을 예정이든 큐에 들어가니 방문 처리해줌.
                    visited_water[x][y] = 1


R, C = map(int, input().split())
visited_water = [[0]*C for _ in range(R)]
visited_swan = [[0]*C for _ in range(R)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]

lake = []
swans = []

# q_w는 물, q_s는 백조, t는 tmp
q_w, q_s, q_wt, q_st = deque(),deque(),deque(),deque()
res = 0
for i in range(R):
    lake_tmp = list(input())
    lake.append(lake_tmp)
    for j in range(C):
        if lake_tmp[j] == 'L':
            swans.append([i,j])
            # visited_water[i][j] = 1
            q_w.append([i,j])
        elif lake_tmp[j] == '.':
            q_w.append([i,j])
            visited_water[i][j] = 1


q_s.append(swans[0])
visited_swan[swans[0][0]][swans[0][1]] = 1
for swan in swans:
    lake[swan[0]][swan[1]] = '.'

while True:
    melting_ice()
    if moving_swan():
        break
    q_s, q_w = q_st, q_wt
    q_st, q_wt = deque(), deque()
    res += 1

print(res)