# baekjoon_14950 정복자

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

N, M, t = map(int, input().split())
edges = []
parents = [i for i in range(N+1)]
res = 0
conquer_cnt = 0
for _ in range(M):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])

for edge in edges:
    a, b, cost = edge
    if finding_parents(parents, a) != finding_parents(parents, b):
        union_parents(a,b)
        res += (cost + conquer_cnt * t)
        conquer_cnt += 1
        if conquer_cnt == N-1:
            break
print(res)


