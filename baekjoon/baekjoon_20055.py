# baekjoon_20055 컨베이어 벨트 위의 로봇

# v1
# def moving_robot():
#     for i in range(2*N-1, -1, -1):
#         if i == (2*N-1):
#             if belt[0] == 0 and belt[i] == 1 and life[0] >= 1:
#                 belt[i] = 0
#                 belt[0] = 1
#                 life[0] -= 1
#         else:
#             if belt[i] == 1 and belt[i+1] == 0 and life[i+1] >= 1:
#                 belt[i] = 0
#                 belt[i+1] = 1
#                 life[i+1] -= 1
#
# def moving_robot2():
#     for i in range(2*N):
#         if life[i] >= 1:
#             life[i] -= 1
#
# N, K = map(int, input().split())
#
# belt = [0]*(2*N)
# life = list(map(int, input().split()))
# life_zero = 0
# step = 0
# robot_cnt = 0
# while True:
#     if life_zero == K:
#         break
#     if robot_cnt == N:
#         moving_robot2()
#     else:
#         moving_robot()
#         if belt[0] == 0 and life[0] >= 1:
#             belt[0] = 1
#             life[0] -= 1
#             robot_cnt += 1
#     life_zero = life.count(0)
#     step += 1
#
# print(step)


# v2
# from collections import deque
#
# N, K = map(int, input().split())
# belt = deque([0]*(2*N))
# life = deque(map(int, input().split()))
# step = 1
#
# while True:
#     belt.rotate(1)
#     life.rotate(1)
#     belt[N-1] = 0
#
#     for i in range(N-2, -1, -1):
#         if belt[i] == 1 and belt[i+1] == 0 and life[i+1] >=1:
#             belt[i] = 0
#             belt[i+1] = 1
#             life[i+1] -= 1
#     belt[N-1] = 0
#
#     if belt[0] == 0 and life[0] >= 1:
#         belt[0] = 1
#         life[0] -= 1
#
#     life_zero = 0
#     for i in range(2*N):
#         if life[i] == 0:
#             life_zero += 1
#     if life_zero >= K:
#         break
#     step += 1
# print(step)

# v3

from collections import deque

N, K = map(int, input().split())
belt = deque()
life = list(map(int, input().split()))
step = 1

for i in range(2*N):
    belt.append([life[i],0])

while True:
    belt.rotate(1)
    belt[N-1][1] = 0

    for i in range(N-2, -1, -1):
        if belt[i][1] == 1 and belt[i+1][1] == 0 and belt[i+1][0] >=1:
            belt[i][1] = 0
            belt[i+1][1] = 1
            belt[i+1][0] -= 1
    belt[N-1][1] = 0

    if belt[0][1] == 0 and belt[0][0] >= 1:
        belt[0][1] = 1
        belt[0][0] -= 1

    life_zero = 0
    for i in range(2*N):
        if belt[i][0] == 0:
            life_zero += 1
    if life_zero >= K:
        break
    step += 1
print(step)