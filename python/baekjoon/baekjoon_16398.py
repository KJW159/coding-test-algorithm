# baekjoon_16398 행성 연결


# v1
def finding_parents(parents, x):
    if parents[x] != x:
        parents[x] = finding_parents(parents, parents[x])
    return parents[x]

def union_parents(x, y):
    p_x = parents[x]
    p_y = parents[y]
    if p_x < p_y:
        parents[p_y] = p_x
    else:
        parents[p_x] = p_y


N = int(input())
cost_table = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)]
edges = []
res = 0

for i in range(N):
    for j in range(i+1, N):
        edges.append([cost_table[i][j], i, j])


edges.sort()

for edge in edges:
    cost, a, b = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a, b)
        res += cost

print(res)