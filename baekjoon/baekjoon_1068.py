# baekjoon_1068 트리

# v1
# def dfs(start, deleted_node):
#     stack = []
#     stack.append(start)
#     leaf_cnt = 0
#
#     while stack:
#         parents = stack.pop()
#         if parents == deleted_node:
#             continue
#         for child in adj_list[parents]:
#             if len(adj_list[child]) != 0:
#                 stack.append(child)
#             elif len(adj_list[child]) == 0 and child != deleted_node:
#                 leaf_cnt += 1
#     return leaf_cnt
#
#
# N = int(input())
# nodes = list(map(int, input().split()))
# adj_list = [[] for _ in range(N)]
# root_nodes = []
# for i in range(N):
#     if nodes[i] == -1:
#         root_nodes.append(i)
#     else:
#         adj_list[nodes[i]].append(i)
# res = 0
# deleted_node = int(input())
# for start in root_nodes:
#     res += dfs(start, deleted_node)
# print(res)

# v2
# def dfs(start, deleted_node):
#     stack = []
#     stack.append(start)
#     leaf_cnt = 0
#
#     while stack:
#         parents = stack.pop()
#         if parents == deleted_node:
#             continue
#         if len(adj_list[parents]) == 1 and deleted_node in adj_list[parents]:
#             leaf_cnt += 1
#             continue
#         for child in adj_list[parents]:
#             if len(adj_list[child]) > 1:
#                 stack.append(child)
#             elif len(adj_list[child]) == 1 and deleted_node in adj_list[child]:
#                 leaf_cnt += 1
#             elif len(adj_list[child]) == 0 and child != deleted_node:
#                 leaf_cnt += 1
#     return leaf_cnt
#
#
# N = int(input())
# nodes = list(map(int, input().split()))
# adj_list = [[] for _ in range(N)]
# root_nodes = []
# for i in range(N):
#     if nodes[i] == -1:
#         root_nodes.append(i)
#     else:
#         adj_list[nodes[i]].append(i)
# res = 0
# deleted_node = int(input())
# for start in root_nodes:
#     res += dfs(start, deleted_node)
# print(res)


# v3
def dfs(start, deleted_node):
    stack = []
    stack.append(start)
    leaf_cnt = 0

    while stack:
        parents = stack.pop()
        if parents == deleted_node:
            continue
        if len(adj_list[parents]) == 1 and deleted_node in adj_list[parents]:
            leaf_cnt += 1
            continue
        for child in adj_list[parents]:
            if len(adj_list[child]) > 1:
                stack.append(child)
            if len(adj_list[child]) == 1:
                if deleted_node not in adj_list[child]:
                    stack.append(child)
                elif deleted_node in adj_list[child]:
                    leaf_cnt += 1
            if len(adj_list[child]) == 0 and child != deleted_node:
                leaf_cnt += 1
    return leaf_cnt


N = int(input())
nodes = list(map(int, input().split()))
adj_list = [[] for _ in range(N)]
root_nodes = []
for i in range(N):
    if nodes[i] == -1:
        root_nodes.append(i)
    else:
        adj_list[nodes[i]].append(i)
res = 0
deleted_node = int(input())
for start in root_nodes:
    res += dfs(start, deleted_node)
print(res)