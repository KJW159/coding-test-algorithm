# baekjoon_14621 나만 안되는 연애




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


N, M = map(int, input().split())
univ = [0]
univ.extend(list(input().split()))
parents = [i for i in range(N+1)]
edges = []
res = 0
edge_num = 0

for _ in range(M):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])

for edge in edges:
    a,b,cost = edge
    if univ[a] != univ[b]:
        if finding_parents(parents, a) != finding_parents(parents, b):
            union_parents(a, b)
            res += cost
            edge_num += 1

if edge_num == N-1:
    print(res)
else:
    print(-1)


