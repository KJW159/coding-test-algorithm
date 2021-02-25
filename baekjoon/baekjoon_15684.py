# baekjoon_15684 사다리 조작

# v1
# def check():
#      for i in range(1, N+1):
#          tmp = i
#          for j in range(1, H+1):
#              if lines[j][tmp] == 1:
#                  tmp += 1
#              elif lines[j][tmp-1] == 1:
#                  tmp -= 1
#          if i != tmp:
#              return False
#      return True
#
#
#
# def dfs(new_num, cnt):
#     global res
#     if res <= cnt:
#         return
#     if new_num == cnt:
#         if check():
#             res = cnt
#         return
#     for i in range(1, N):
#         for j in range(1, H+1):
#             # if lines[j][i-1] == 0 and lines[j][i] == 0 and lines[j][i+1] == 0:
#             if lines[j][i] == 0:
#                 lines[j][i] = 1
#                 dfs(new_num, cnt+1)
#                 lines[j][i] = 0
#
#
# N, M, H = map(int, input().split())
# lines = [[0]*(N+1) for _ in range(H+1)]
# res = 5
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     lines[a][b] = 1
#
# for i in range(4):
#     dfs(i, 0)
#     if res < 4:
#         print(res)
#         break
# if res > 4:
#     print(-1)

# v2
def check():
    for i in range(1, N + 1):
        tmp = i
        for j in range(1, H + 1):
            if lines[j][tmp] == 1:
                tmp += 1
            elif lines[j][tmp - 1] == 1:
                tmp -= 1
        if i != tmp:
            return False
    return True


def dfs(new_num, cnt):
    global res
    if res <= cnt:
        return
    if new_num == cnt:
        if check():
            res = cnt
        return
    for i in range(1, N):
        for j in range(1, H + 1):
            if lines[j][i-1] == 0 and lines[j][i] == 0 and lines[j][i+1] == 0:
            # if lines[j][i] == 0:
                lines[j][i] = 1
                dfs(new_num, cnt + 1)
                lines[j][i] = 0


N, M, H = map(int, input().split())
lines = [[0] * (N + 1) for _ in range(H + 1)]
res = 5

for _ in range(M):
    a, b = map(int, input().split())
    lines[a][b] = 1

for i in range(4):
    dfs(i, 0)
    if res < 4:
        print(res)
        break
if res > 4:
    print(-1)
