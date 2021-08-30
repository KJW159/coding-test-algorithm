# baekjoon_1167 트리의 지름

# v1
# def dfs(cur_node, dist):
#     global res
#     if dist > res:
#         res = dist
#
#     for next_node, next_dist in adj_list[cur_node]:
#         if visited[next_node] == 0:
#             visited[next_node] = 1
#             dfs(next_node, dist+next_dist)
#             visited[next_node] = 0
#
#
# V = int(input())
# adj_list = [[] for _ in range(V+1)]
# res = 0
# for _ in range(V):
#     tmp = list(map(int, input().split()))
#     for i in range(1, len(tmp)-1, 2):
#         adj_list[tmp[0]].append([tmp[i], tmp[i+1]])
#
# visited = [0]*(V+1)
# for i in range(1, V+1):
#     visited[i] = 1
#     dfs(i,0)
#     visited[i] = 0
# print(res)


# v2
def dfs(cur_node, visited):
    for next_node, next_dist in adj_list[cur_node]:
        if visited[next_node] == 0:
            visited[next_node] = visited[cur_node] + next_dist
            dfs(next_node, visited)


V = int(input())
adj_list = [[] for _ in range(V+1)]
res = 0
for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        adj_list[tmp[0]].append([tmp[i], tmp[i+1]])

visited1 = [0]*(V+1)
dfs(1, visited1)
visited1[1] = 0

max_dist = 0
max_index = 0

for i in range(1, V+1):
    if max_dist < visited1[i]:
        max_dist = visited1[i]
        max_index = i


visited2 = [0]*(V+1)
dfs(max_index, visited2)
visited2[max_index] = 0
print(max(visited2))


