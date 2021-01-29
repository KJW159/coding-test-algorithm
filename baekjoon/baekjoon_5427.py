# baekjoon_5427 불

#v1
# from collections import deque
#
#
# def bfs(fire_positions, man):
#     dx = [0,-1,0,1]
#     dy = [-1,0,1,0]
#
#
#     queue_f = deque()
#     queue_m = deque()
#     for fire in fire_positions:
#         queue_f.append([fire[0], fire[1]])
#         visited[fire[0]][fire[1]] = 0
#     # queue.append([man[0], man[1]])
#     queue_m.append([man[0], man[1]])
#     visited[man[0]][man[1]] = 0
#     escape = False
#     while True:
#         m_i, m_j = queue_m.popleft()
#         if m_i == 0 or m_i == h or m_j == 0 or m_j == w:
#             escape = True
#             break
#         f_i, f_j = queue_f.popleft()
#         for f in range(4):
#             f_x = f_i + dx[f]
#             f_y = f_j + dy[f]
#             if 0 <= f_x < h and 0 <= f_y < w:
#                 if visited[f_x][f_y] == -1 and arr[f_x][f_y] == '.':
#                     queue_f.append([f_x, f_y])
#                     visited[f_x][f_y] = 0
#                     arr[f_x][f_y] = '*'
#         for m in range(4):
#             m_x = m_i + dx[m]
#             m_y = m_j + dy[m]
#             if 0 <= m_x < h and 0 <= m_y < w:
#                 if visited[m_x][m_y] == -1 and arr[m_x][m_y] == '.':
#                     queue_m.append([m_x, m_y])
#                     visited[m_x][m_y] = visited[m_i][m_j] + 1
#     return escape
#
# T = int(input())
#
# for tc in range(T):
#     w, h = map(int, input().split())
#     arr = [list(input()) for __ in range(h)]
#     fire_positions = []
#     visited = [[-1] * w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '*':
#                 fire_positions.append([i,j])
#             if arr[i][j] == '@':
#                 man_position = [i,j]
#
#     res = bfs(fire_positions, man_position)
#     if res:
#         min_time = -1
#         for i in range(h):
#             for j in range(w):
#                 if visited[i][j] > min_time:
#                     min_time = visited[i][j]
#         res = min_time
#     else:
#         res = 'IMPOSSIBLE'
#     print(res)

# v2
# from collections import deque
#
# def bfs(fire_positions, man):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     queue = deque()
#     for fire in fire_positions:
#         queue.append([fire[0], fire[1], '*'])
#         visited[fire[0]][fire[1]] = 0
#     queue.append([man[0], man[1], '@'])
#     visited[man[0]][man[1]] = 1
#     escape = False
#
#     while queue:
#         s_i, s_j, thing = queue.popleft()
#         if thing == '@':
#             if s_i == 0 or s_i == h-1 or s_j == 0 or s_j == w-1:
#                 escape = True
#                 break
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < h and 0 <= y < w:
#                 if thing == '*' and visited[x][y] == -1 and arr[x][y] == '.':
#                     queue.append([x, y, '*'])
#                     visited[x][y] = 0
#                     arr[x][y] = '*'
#                 if thing == '@' and visited[x][y] == -1 and arr[x][y] == '.':
#                     queue.append([x, y, '@'])
#                     visited[x][y] = visited[s_i][s_j] + 1
#     return escape
#
# T = int(input())
#
# for tc in range(T):
#     w, h = map(int, input().split())
#     arr = [list(input()) for __ in range(h)]
#     fire_positions = []
#     man_position = []
#     visited = [[-1] * w for _ in range(h)]
#     res = False
#     min_time = -1
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '*':
#                 fire_positions.append([i,j])
#             if arr[i][j] == '@':
#                 man_position = [i, j]
#     res = bfs(fire_positions, man_position)
#     if res:
#         for i in range(h):
#             for j in range(w):
#                 if visited[i][j] > min_time:
#                     min_time = visited[i][j]
#         res = min_time
#     else:
#         res = 'IMPOSSIBLE'
#     print(res)

# v3

# from collections import deque
#
# def bfs(fire_positions, man):
#     dx = [0, -1, 0, 1]
#     dy = [-1, 0, 1, 0]
#
#     queue = deque()
#     for fire in fire_positions:
#         queue.append([fire[0], fire[1], '*'])
#         visited[fire[0]][fire[1]] = 0
#     queue.append([man[0], man[1], '@'])
#     visited[man[0]][man[1]] = 0
#     escape = False
#     res_tmp = 0
#     while queue:
#         s_i, s_j, thing = queue.popleft()
#         if thing == '@':
#             if s_i == 0 or s_i == h-1 or s_j == 0 or s_j == w-1:
#                 res_tmp = visited[s_i][s_j]
#                 escape = True
#                 break
#         for c in range(4):
#             x = s_i + dx[c]
#             y = s_j + dy[c]
#             if 0 <= x < h and 0 <= y < w:
#                 if thing == '*' and visited[x][y] == -1 and arr[x][y] != '#':
#                     queue.append([x, y, '*'])
#                     visited[x][y] = 0
#                     arr[x][y] = '*'
#                 if thing == '@' and visited[x][y] == -1 and arr[x][y] == '.':
#                     queue.append([x, y, '@'])
#                     visited[x][y] = visited[s_i][s_j] + 1
#
#     return escape, res_tmp
#
# T = int(input())
#
# for tc in range(T):
#     w, h = map(int, input().split())
#     arr = [list(input()) for __ in range(h)]
#     fire_positions = []
#     man_position = []
#     visited = [[-1] * w for _ in range(h)]
#     res = False
#     min_time = -1
#     for i in range(h):
#         for j in range(w):
#             if arr[i][j] == '*':
#                 fire_positions.append([i,j])
#             if arr[i][j] == '@':
#                 man_position = [i, j]
#     res, step = bfs(fire_positions, man_position)
#
#     if res:
#         ans = step + 1
#     else:
#         ans = 'IMPOSSIBLE'
#     print(ans)


# v4
from collections import deque

def bfs(fire_positions, man):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    queue = deque()
    for fire in fire_positions:
        queue.append([fire[0], fire[1], '*'])
        visited[fire[0]][fire[1]] = 0
    queue.append([man[0], man[1], '@'])
    visited[man[0]][man[1]] = 0
    escape = False
    res_tmp = 0
    while queue:
        s_i, s_j, thing = queue.popleft()
        if thing == '@':
            if s_i == 0 or s_i == h-1 or s_j == 0 or s_j == w-1:
                res_tmp = visited[s_i][s_j]
                escape = True
                break
        for c in range(4):
            x = s_i + dx[c]
            y = s_j + dy[c]
            if 0 <= x < h and 0 <= y < w:
                if visited[x][y] == -1 and arr[x][y] == '.':
                    if thing == '*':
                        queue.append([x, y, '*'])
                        visited[x][y] = 0
                        # arr[x][y] = '*'
                    if thing == '@':
                        queue.append([x, y, '@'])
                        visited[x][y] = visited[s_i][s_j] + 1

    return escape, res_tmp

T = int(input())

for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(input()) for __ in range(h)]
    fire_positions = []
    man_position = []
    visited = [[-1] * w for _ in range(h)]
    res = False
    min_time = -1
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_positions.append([i,j])
            if arr[i][j] == '@':
                man_position = [i, j]
    res, step = bfs(fire_positions, man_position)

    if res:
        ans = step + 1
    else:
        ans = 'IMPOSSIBLE'
    print(ans)
