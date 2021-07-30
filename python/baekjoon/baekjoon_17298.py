# baekjoon_17298 오큰수

# v1
# import heapq
#
# def NGE(idx):
#     cur_num = A[idx]
#     hq = []
#
#     for next in range(idx+1, N):
#         # heapq.heappush(hq, [-A[next], next])
#         heapq.heappush(hq, [next, -A[next]])
#
#     for _ in range(N-1-idx):
#         next_idx, next_num = heapq.heappop(hq)
#         if -next_num > cur_num:
#             return -next_num
#     return -1
#
# N = int(input())
# A = list(map(int, input().split()))
#
# for i in range(N-1):
#     print(NGE(i), end=" ")
# print(-1)


# v2
# import heapq, sys
#
# input = sys.stdin.readline
#
# def NGE(idx):
#     cur_num = A[idx]
#     hq = []
#
#     for next_idx in range(idx+1, N):
#         heapq.heappush(hq, [next_idx, -A[next_idx]])
#
#     for _ in range(N-1-idx):
#         next_idx, next_num = heapq.heappop(hq)
#         if -next_num > cur_num:
#             return -next_num
#     return -1
#
#
# N = int(input())
# A = list(map(int, input().split()))
#
# for i in range(N-1):
#     print(NGE(i), end=" ")
# print(-1)

# v3
# import math, sys
#
# input = sys.stdin.readline
#
# def NGE(idx):
#     cur_num = A[idx]
#     next_num = 0
#     next_idx = math.inf
#
#     for i in range(idx+1, N):
#         num = A[i]
#         if num > cur_num and next_num < num:
#             if next_idx > i:
#                 next_num = num
#                 next_idx = i
#     if next_num != 0:
#         return next_num
#     else:
#         return -1
#
#
# N = int(input())
# A = list(map(int, input().split()))
#
# for i in range(N-1):
#     print(NGE(i), end=" ")
# print(-1)


# v4
# import sys
#
# input = sys.stdin.readline
#
#
# def NGE(idx):
#     cur_num = A[idx]
#
#     for i in range(idx+1, N):
#         num = A[i]
#         if num > cur_num:
#             return num
#     return -1
#
#
#
# N = int(input())
# A = list(map(int, input().split()))
#
# for i in range(N-1):
#     print(NGE(i), end=" ")
# print(-1)


# v5
#
# import sys
#
# input = sys.stdin.readline
#
# def dfs(cur_idx, cur_num):
#     stack = []
#     stack.append(cur_idx+1)
#
#     while stack:
#         pre_idx = stack.pop()
#         if res[pre_idx] > cur_num:
#             return res[pre_idx]
#         else:
#             if pre_idx+1 < N-1:
#                 stack.append(pre_idx+1)
#     return -1
#
# N = int(input())
# A = list(map(int, input().split()))
# res = [0]*N
# idx = [0]*N
#
#
# for i in range(N-2, -1, -1):
#     big_num = A.pop()
#     if A[i] < big_num:
#         res[i] = big_num
#         idx[i] = i+1
#     else:
#         res[i] = dfs(i, A[i])
#
# for i in range(N-1):
#     print(res[i], end=" ")
# print(-1)


# v6

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
res = [-1]*N
res[N-1] = -1
stack = [0]

for i in range(1, N):
    while stack:
        if A[stack[-1]] < A[i]:
            cur_idx = stack.pop()
            res[cur_idx] = A[i]
        else:
            break
    stack.append(i)
for i in range(N):
    print(res[i], end=" ")
