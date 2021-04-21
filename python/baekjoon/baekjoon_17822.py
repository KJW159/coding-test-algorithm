# # baekjoon_17822 원판 돌리기
# from collections import deque
#
# def rotating_circle(x,d,k):
#     for i in range(1, N+1):
#         if i % x == 0:
#             if d == 0:
#                 tmp = k
#             else:
#                 tmp = -k
#             circle[i].rotate(tmp)
#
# N, M, T = map(int, input().split())
# circle = [[0]*M]
# for _ in range(N):
#     circle.append(deque(map(int, input().split())))
# x, d, k = map(int, input().split())
#
#
# for t in range(T):
#     rotating_circle(x,d,k)
#     erased_num = set()
#     trg = False
#     for i in range(1, N+1):
#         for j in range(M):
#             # 좌우 체크
#             left = (j-1)%M
#             right = (j+1)%M
#             if circle[i][left] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((i,left))
#                 trg = True
#             if circle[i][right] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((i,right))
#                 trg = True
#             # 위, 아래 체크
#             down = (j+1) % N
#             up = (j-1) % N
#             if circle[up][i] == circle[j][i]:
#                 erased_num.add((j,i))
#                 erased_num.add((up,i))
#                 trg = True
#             if circle[down][i] == circle[j][i]:
#                 erased_num.add((j,i))
#                 erased_num.add((down,i))
#                 trg = True
#     if trg:
#         for nx, ny in erased_num:
#             circle[nx][ny] = 0
#     else:
#         total_num = 0
#         cnt = 0
#         changed_num = set()
#         for i in range(1, N+1):
#             for j in range(M):
#                 if total_num != 0:
#                     total_num += circle[i][j]
#                     cnt += 1
#                     changed_num.add([i,j])
#         avg = total_num / cnt
#         for nx , ny in changed_num:
#             if circle[nx][ny] < avg:
#                 circle[nx][ny] += 1
#             if circle[nx][ny] > avg:
#                 circle[nx][ny] -= 1
# res = 0
# for i in range(1, N+1):
#     for j in range(M):
#         if circle[i][j] != 0:
#             res += circle[i][j]
# print(res)
#
#
#
# baekjoon_17822 원판 돌리기
# from collections import deque
#
# def rotating_circle(x,d,k):
#     for i in range(1, N+1):
#         if i % x == 0:
#             if d == 0:
#                 tmp = k
#             else:
#                 tmp = -k
#             circle[i].rotate(tmp)
#
# N, M, T = map(int, input().split())
# circle = [[0]*M]
# for _ in range(N):
#     circle.append(deque(map(int, input().split())))
# x, d, k = map(int, input().split())
#
#
# for t in range(T):
#     rotating_circle(x,d,k)
#     erased_num = set()
#     trg = False
#     for i in range(1, N+1):
#         for j in range(M):
#             # 좌우 체크
#             left = (j-1)%M
#             right = (j+1)%M
#             if circle[i][left] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((i,left))
#                 trg = True
#             if circle[i][right] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((i,right))
#                 trg = True
#
#     for i in range(1, N+1):
#          for j in range(M):
#             # 위, 아래 체크
#             down = (i+1) % N
#             up = (i-1) % N
#             if up == 0 and i == 1:
#                 up = 1
#
#             if circle[up][j] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((up,j))
#                 trg = True
#             if circle[down][j] == circle[i][j]:
#                 erased_num.add((i,j))
#                 erased_num.add((down,j))
#                 trg = True
#     if trg:
#         for nx, ny in erased_num:
#             circle[nx][ny] = 0
#     else:
#         total_num = 0
#         cnt = 0
#         changed_num = set()
#         for i in range(1, N+1):
#             for j in range(M):
#                 if total_num != 0:
#                     total_num += circle[i][j]
#                     cnt += 1
#                     changed_num.add([i,j])
#         avg = total_num / cnt
#         for nx ,ny in changed_num:
#             if circle[nx][ny] < avg:
#                 circle[nx][ny] += 1
#             if circle[nx][ny] > avg:
#                 circle[nx][ny] -= 1
# res = 0
# for i in range(1, N+1):
#     for j in range(M):
#         if circle[i][j] != 0:
#             res += circle[i][j]
#
# print(res)


# v3

from collections import deque

def rotating_circle(x,d,k):
    for i in range(1, N+1):
        if i % x == 0:
            if d == 0:
                tmp = k
            else:
                tmp = -k
            circle[i].rotate(tmp)

N, M, T = map(int, input().split())
circle = [[0]*M]
for _ in range(N):
    circle.append(deque(map(int, input().split())))
order_rotating = []
for _ in range(T):
    order_rotating.append(list(map(int, input().split())))

for t in range(T):
    x,d,k = order_rotating[t]
    rotating_circle(x,d,k)
    erased_num = set()
    trg = False

    for i in range(1, N+1):
        for j in range(M):
            # 좌우 체크
            left = (j-1)%M
            right = (j+1)%M
            if circle[i][j] != 0:
                if circle[i][left] == circle[i][j]:
                    erased_num.add((i,j))
                    erased_num.add((i,left))
                    trg = True
                if circle[i][right] == circle[i][j]:
                    erased_num.add((i,j))
                    erased_num.add((i,right))
                    trg = True

    for i in range(1, N+1):
         for j in range(M):
            # 위, 아래 체크
            down = (i+1)
            up = (i-1)
            if circle[i][j] != 0:
                if 1 <= up < N+1:
                    if circle[up][j] == circle[i][j]:
                        erased_num.add((i,j))
                        erased_num.add((up,j))
                        trg = True
                if 1 <= down < N+1:
                    if circle[down][j] == circle[i][j]:
                        erased_num.add((i,j))
                        erased_num.add((down,j))
                        trg = True
    if trg:
        for nx, ny in erased_num:
            circle[nx][ny] = 0
    else:
        total_num = 0
        cnt = 0
        changed_num = set()
        for i in range(1, N+1):
            for j in range(M):
                if circle[i][j] != 0:
                    total_num += circle[i][j]
                    cnt += 1
                    changed_num.add((i,j))
        if cnt != 0:
            avg = total_num / cnt
            for nx, ny in changed_num:
                if circle[nx][ny] < avg:
                    circle[nx][ny] += 1
                elif circle[nx][ny] > avg:
                    circle[nx][ny] -= 1

res = 0
for i in range(1, N+1):
    for j in range(M):
        if circle[i][j] != 0:
            res += circle[i][j]
print(res)