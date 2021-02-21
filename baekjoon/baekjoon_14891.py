# baekjoon_14891 톱니바퀴

# v1
# from collections import deque
#
# def checking(i):
#     if gears[i][2] == gears[i+1][6]:
#         return 0
#     else:
#         return 1
#
# def rotating(gear_num, direction):
#     queue = deque()
#     visited = [0]*4
#     queue.append([gear_num, direction, 1])
#     visited[gear_num] = 1
#     while queue:
#         gear, di, rotated = queue.popleft()
#         if 0 <= gear-1 < 4 and visited[gear-1] == 0:
#             if rotated == 1 and check_gear[gear-1] == 1:
#                 gears[gear-1].rotate(-di)
#                 queue.append([gear-1, -di, 1])
#                 visited[gear-1] = 1
#             elif rotated == 1 and check_gear[gear-1] == 0:
#                 queue.append([gear-1, -di, 0])
#                 visited[gear-1] = 1
#             elif rotated == 0:
#                 queue.append([gear - 1, -di, 0])
#                 visited[gear-1] = 1
#         if 0 <= gear+1 < 4 and visited[gear+1] == 0:
#             if rotated == 1 and check_gear[gear] == 1:
#                 gears[gear+1].rotate(-di)
#                 queue.append([gear+1, -di, 1])
#                 visited[gear+1] = 1
#             elif rotated == 1 and check_gear[gear] == 0:
#                 queue.append([gear+1, -di, 0])
#                 visited[gear+1] = 1
#             elif rotated == 0:
#                 queue.append([gear+1, -di, 0])
#                 visited[gear+1] = 1
#
# gears = [deque(map(int, input())) for _ in range(4)]
# K = int(input())
# rotation = [list(map(int, input().split())) for _ in range(K)]
#
#
#
# for k in range(K):
#     gear_num, direction = rotation[k]
#     gear_num -= 1
#     gears[gear_num].rotate(direction)
#     check_gear = []
#     for i in range(3):
#         check_gear.append(checking(i))
#     rotating(gear_num, direction)
# res = 0
# for c in range(4):
#     if gears[c][0]:
#         res += 2**c
#
# print(res)

# v2
# from collections import deque
#
# def checking(i):
#     if gears[i][2] == gears[i+1][6]:
#         return 0
#     else:
#         return 1
#
# def rotating(gear_num, direction):
#     queue = deque()
#     visited = [0]*4
#     queue.append([gear_num, direction, 1])
#     visited[gear_num] = 1
#     while queue:
#         gear, di, rotated = queue.popleft()
#         if 0 <= gear-1 < 4 and visited[gear-1] == 0:
#             if rotated == 1 and check_gear[gear-1] == 1:
#                 gears[gear-1].rotate(-di)
#                 queue.append([gear-1, -di, 1])
#                 visited[gear-1] = 1
#             elif rotated == 1 and check_gear[gear-1] == 0:
#                 queue.append([gear-1, -di, 0])
#                 visited[gear-1] = 1
#             elif rotated == 0:
#                 queue.append([gear - 1, -di, 0])
#                 visited[gear-1] = 1
#         if 0 <= gear+1 < 4 and visited[gear+1] == 0:
#             if rotated == 1 and check_gear[gear] == 1:
#                 gears[gear+1].rotate(-di)
#                 queue.append([gear+1, -di, 1])
#                 visited[gear+1] = 1
#             elif rotated == 1 and check_gear[gear] == 0:
#                 queue.append([gear+1, -di, 0])
#                 visited[gear+1] = 1
#             elif rotated == 0:
#                 queue.append([gear+1, -di, 0])
#                 visited[gear+1] = 1
#
# gears = [deque(map(int, input())) for _ in range(4)]
# K = int(input())
# rotation = [list(map(int, input().split())) for _ in range(K)]
#
#
#
# for k in range(K):
#     check_gear = []
#     for i in range(3):
#         check_gear.append(checking(i))
#     gear_num, direction = rotation[k]
#     gear_num -= 1
#     gears[gear_num].rotate(direction)
#     rotating(gear_num, direction)
# res = 0
# for c in range(4):
#     if gears[c][0]:
#         res += 2**c
#
# print(res)

# v4
from collections import deque

def checking(i):
    if gears[i][2] == gears[i+1][6]:
        return 0
    else:
        return 1

def rotating(gear_num, direction):
    stack = []
    visited = [0]*4
    stack.append([gear_num, direction])
    visited[gear_num] = 1
    while stack:
        gear, di = stack.pop()
        if 0 <= gear-1 < 4 and visited[gear-1] == 0:
            if check_gear[gear-1] == 1:
                gears[gear-1].rotate(-di)
                stack.append([gear-1, -di])
                visited[gear-1] = 1
        if 0 <= gear+1 < 4 and visited[gear+1] == 0:
            if check_gear[gear] == 1:
                gears[gear+1].rotate(-di)
                stack.append([gear+1, -di])
                visited[gear+1] = 1

gears = [deque(map(int, input())) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

for k in range(K):
    check_gear = []
    for i in range(3):
        check_gear.append(checking(i))
    gear_num, direction = rotation[k]
    gear_num -= 1
    gears[gear_num].rotate(direction)
    rotating(gear_num, direction)
res = 0
for c in range(4):
    if gears[c][0]:
        res += 2**c

print(res)

