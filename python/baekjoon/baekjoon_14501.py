# baekjoon_14501 퇴사
# import sys
#
#
# # v1
# def time_dfs(time_pi,idx):
#     stack = []
#     stack.append(time_pi)
#     # idx = timetable.index(time_pi)
#     sum_pi = 0
#
#     # v1
#     # while stack:
#     #     ti, pi = stack.pop()
#     #     idx += ti
#     #     if idx > N:
#     #         break
#     #     if (idx-1) < N:
#     #         sum_pi += pi
#     #         stack.append(timetable[idx])
#     # return sum_pi
#
#     # v2
#     # while stack:
#     #     ti, pi = stack.pop()
#     #     idx += ti
#     #     if (idx-1) < N:
#     #         sum_pi += pi
#     #     if idx >= N:
#     #         break
#     #     else:
#     #         stack.append(timetable[idx])
#     # return sum_pi
#
#     # v3
#     while stack:
#         ti, pi = stack.pop()
#         idx += ti
#         if idx < N:
#             sum_pi += pi
#         if idx >= N:
#             return sum_pi
#         else:
#             stack.append(timetable[idx])
#
#
# N = int(input())
# timetable = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
#
# max_pi = 0
# idx = 0
# for time_pi in timetable:
#     pi_tmp = time_dfs(time_pi, idx)
#     idx += 1
#     if pi_tmp > max_pi:
#         max_pi = pi_tmp
#
# print(max_pi)




# re-v1

# def dfs(start):
#     stack = []
#     stack.append(start)
#     money = table[start][1]
#
#     while stack:
#         start = stack.pop()
#         next_day = start + table[start][0]
#         if next_day < N:
#             if next_day + table[next_day][0] <= N:
#                 stack.append(next_day)
#                 money += table[next_day][1]
#     return money
#
#
# N = int(input())
# table = []
#
# for i in range(N):
#     ti, pi = map(int, input().split())
#     table.append([ti, pi])
#
# res = 0
# for i in range(N):
#     if i+table[i][0] > N:
#         continue
#     res = max(res, dfs(i))
# print(res)


# re-v2

# def dfs(start, money):
#     global res
#
#     if start + table[start][0] >= N:
#         res = max(res, money)
#         return
#     else:
#         money += table[start][1]
#         dfs(start+table[start][0], money)
#         dfs(start+1, money-table[start][1])
#
#
# N = int(input())
# table = []
#
# for i in range(N):
#     ti, pi = map(int, input().split())
#     table.append([ti, pi])
#
# res = 0
# for i in range(N):
#     dfs(i,0)
# print(res)


# re -v3
# def dfs(start, money):
#     global res
#
#     if start + table[start][0] > N:
#         res = max(res, money)
#         return
#
#     if start + table[start][0] == N:
#         money += table[start][1]
#         res = max(res, money)
#         return
#
#     if start + table[start][0] < N:
#         dfs(start+table[start][0], money+table[start][1])
#         dfs(start+1, money)
#
#
# N = int(input())
# table = []
#
# for i in range(N):
#     ti, pi = map(int, input().split())
#     table.append([ti, pi])
#
# res = 0
# for i in range(N):
#     dfs(i,0)
# print(res)

# re-v4
def dfs(start, money):
    global res

    if start > N:
        # res = max(res, money)
        return

    if start == N:
        # money += table[start][1]
        res = max(res, money)
        return

    if start < N:
        dfs(start+table[start][0], money+table[start][1])
        dfs(start+1, money)


N = int(input())
table = []

for i in range(N):
    ti, pi = map(int, input().split())
    table.append([ti, pi])

res = 0
dfs(0,0)
print(res)