# baekjoon_16964 DFS 스페셜 저지

# v1 양방향이였음. 그리고 문제도 예제2만 보고 풀고 있었는데, 예제 3이랑 같이 보면 2,3둘중에 먼저 어느것 방문해도 맞는 걸로 해야함.
# 조건
# 양방향 그래프, 트리, 시작 정점은 1

#v1
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# res = 1
# idx = 0
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#
# true_seq = list(map(int, input().split()))
#
# stack = [1]
# visited[1] = 1
#
# while stack:
#     pre_node = stack.pop()
#     if true_seq[idx] != pre_node:
#         res = 0
#         break
#     for next_node in adj_list[pre_node]:
#         if visited[next_node] == 0:
#             idx += 1
#             stack.append(next_node)
#             visited[next_node] = 1
#
# print(res)


# v2
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# res = 1
# idx = -1
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#
# true_seq = list(map(int, input().split()))
#
# stack = [1]
# visited[1] = 1
#
# while stack:
#     pre_node = stack.pop()
#     idx += 1
#     if true_seq[idx] != pre_node:
#         res = 0
#         break
#     for next_node in adj_list[pre_node]:
#         if visited[next_node] == 0:
#             # idx += 1
#             stack.append(next_node)
#             visited[next_node] = 1
#
# print(res)



# v3

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# adj_list = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# res = 1
# idx = 0
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#
# true_seq = list(map(int, input().split()))
#
# stack = [1]
# visited[1] = 1
#
# while stack:
#     pre_node = stack.pop()
#     idx += 1
#     next_node = true_seq[idx]
#     if next_node in adj_list[pre_node]:
#         if visited[next_node] == 0:
#             stack.append(next_node)
#             visited[next_node] = 1
#     else:
#         res = 0
#         break
#
# print(res)

# idx 이동함. 같은 게 안에 있는 경우에는 킵해두고 for문 끝나고 넣음.
# 없으면 그냥 나가버림.


#v4

import sys

input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N+1)]
visited = [0]*(N+1)
res = 1
idx = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)

true_seq = list(map(int, input().split()))

stack = [1]
visited[1] = 1

while stack:
    pre_node = stack.pop()
    idx += 1
    next_node = true_seq[idx]
    if next_node in adj_list[pre_node]:
        if visited[next_node] == 0:
            stack.append(next_node)
            visited[next_node] = 1
    else:
        res = 0
        break

print(res)