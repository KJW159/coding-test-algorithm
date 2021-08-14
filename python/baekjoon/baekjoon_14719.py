# baekjoon_14719 빗물

# v1
# def checking_wall(s_i, s_j, direction):
#     stack = []
#     stack.append(s_j)
#
#     while stack:
#         s_j = stack.pop()
#         y = s_j + dy[direction]
#         if 0 <= y < M:
#             if world[s_i][y] == 1 or world[s_i][y] == -1:
#                 return True
#             if world[s_i][y] == 0:
#                 stack.append(y)
#     return False
#
#
#
# N, M = map(int, input().split())
# world = [[0]*M for _ in range(N)]
# rain = list(map(int, input().split()))
#
# res = 0
# dy = [-1, 1]
#
# for i in range(M):
#     for j in range(N-1, N-rain[i]-1, -1):
#         world[j][i] = -1
#
#
# for i in range(N):
#     for j in range(1, M-1):
#         if world[i][j] == 0:
#             trg1 = checking_wall(i, j, 0)
#             trg2 = checking_wall(i, j, 1)
#             if trg1 and trg2:
#                 world[i][j] = 1
#                 res += 1
# print(res)


# v2
# N, M = map(int, input().split())
# world = [[0]*M for _ in range(N)]
# rain = list(map(int, input().split()))
#
# res = 0
# dy = [-1, 1]
#
# for i in range(M):
#     for j in range(N-1, N-rain[i]-1, -1):
#         world[j][i] = -1
#
#
# for i in range(N):
#     for j in range(1, M-1):
#         if world[i][j] == 0:
#             trg = [False, False]
#             for k in range(2):
#                 y = j
#                 while True:
#                     y += dy[k]
#                     if 0 <= y < M:
#                         if world[i][y] == 0:
#                             continue
#                         if world[i][y] == -1 or world[i][y] == 1:
#                             trg[k] = True
#                             break
#                     else:
#                         break
#             if trg[0] and trg[1]:
#                 world[i][j] = 1
#                 res += 1
# print(res)



# v3
N, M = map(int, input().split())
wall_height = list(map(int, input().split()))
res = 0

for i in range(1, M-1):
    left_height = wall_height[i]
    for j in range(i-1, -1, -1):
        if wall_height[j] > left_height:
            left_height = wall_height[j]

    right_height = wall_height[i]
    for j in range(i+1, M):
        if wall_height[j] > right_height:
            right_height = wall_height[j]

    min_height = min(left_height, right_height)
    res += (min_height-wall_height[i])
print(res)