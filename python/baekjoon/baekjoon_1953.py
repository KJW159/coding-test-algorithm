# baekjoon_1953 팀배분


# v1
def dfs():
    stack = [1]
    visited[1] = 1
    for i in range(1, N+1):
        if visited[i] == 0:
            stack.append(i)
            visited[i] = 1
        while stack:
            cur_num = stack.pop()
            team_num = visited[cur_num]
            for j in adj_list[cur_num]:
                if visited[j] == 0:
                    stack.append(j)
                    if team_num == 1:
                        visited[j] = 2
                    elif team_num == 2:
                        visited[j] = 1


N = int(input())
visited = [0]*(N+1)
adj_list = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in tmp[1:]:
        adj_list[i].append(j)

dfs()
team_1 = []
team_2 = []
for i in range(1, N+1):
    if visited[i] == 1:
        team_1.append(i)
    else:
        team_2.append(i)

print(len(team_1))
print(*team_1)
print(len(team_2))
print(*team_2)