# baekjoon_9466 텀 프로젝트

# v1
# def dfs(start):
#     visited_tmp = visited[:]
#     stack = []
#     stack.append(start)
#     visited_tmp[start] = 1
#     team_tmp = [start]
#     trg_tmp = False
#
#     while stack:
#         people = stack.pop()
#         choice = students[people]
#         if visited_tmp[choice] == 1 and choice != start:
#             break
#         if visited_tmp[choice] == 0:
#             stack.append(choice)
#             visited_tmp[choice] = 1
#             team_tmp.append(choice)
#         if visited_tmp[choice] == 1 and choice == start:
#             trg_tmp = True
#             break
#     return trg_tmp, team_tmp
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     students = [0]
#     students.extend(list(map(int, input().split())))
#     visited = [0]*(N+1)
#     team_num = 0
#
#     for start in range(1, N+1):
#         if visited[start] == 0:
#             trg, team = dfs(start)
#             if trg:
#                 team_num += len(team)
#                 for t in team:
#                     visited[t] = 1
#     print(N-team_num)


# v2
# def dfs(start):
#     stack = []
#     stack.append(start)
#     visited_tmp = [start]
#     # team_tmp = [start]
#     trg_tmp = False
#
#     while stack:
#         people = stack.pop()
#         choice = students[people]
#         if visited[choice] == 1 and choice != start:
#             break
#         if choice not in visited_tmp:
#             stack.append(choice)
#             visited_tmp.append(choice)
#         if choice in visited_tmp and choice == start:
#             trg_tmp = True
#             break
#     return trg_tmp, visited_tmp
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     students = [0]
#     students.extend(list(map(int, input().split())))
#     visited = [0]*(N+1)
#     team_num = 0
#
#     for start in range(1, N+1):
#         if visited[start] == 0:
#             trg, team = dfs(start)
#             if trg:
#                 team_num += len(team)
#                 for t in team:
#                     visited[t] = 1
#     print(N-team_num)

# v3
# def dfs(start):
#     stack = []
#     visited_tmp = [0] * (N + 1)
#
#     stack.append(start)
#     visited_tmp[start] = 1
#     trg_tmp = False
#
#     while stack:
#         people = stack.pop()
#         choice = students[people]
#         if visited[choice] == 1 and choice != start:
#             break
#         if visited_tmp[choice] == 0:
#             stack.append(choice)
#             visited_tmp[choice] = 1
#         if visited_tmp[choice] == 1 and choice == start:
#             trg_tmp = True
#             break
#     return trg_tmp, visited_tmp
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     students = [0]
#     students.extend(list(map(int, input().split())))
#     visited = [0]*(N+1)
#     team_num = 0
#
#     for start in range(1, N+1):
#         if visited[start] == 0:
#             trg, team = dfs(start)
#             if trg:
#                 for t in range(1, N+1):
#                     if team[t] == 0 or visited[t] == 1:
#                         continue
#                     if visited[t] == 0 and team[t] == 1:
#                         visited[t] = 1
#                         team_num += 1
#     print(N-team_num)


# v4
# import sys
#
# def dfs(start):
#     stack = []
#     stack.append(start)
#     visited_tmp = set()
#     visited_tmp.add(start)
#     trg_tmp = False
#
#     while stack:
#         people = stack.pop()
#         choice = students[people]
#         if visited[choice] == 1 and choice != start:
#             break
#         if choice not in visited_tmp:
#             stack.append(choice)
#             visited_tmp.add(choice)
#         if choice in visited_tmp and choice == start:
#             trg_tmp = True
#             break
#     return trg_tmp, visited_tmp
#
# inputs = sys.stdin.readline
#
# T = int(inputs())
# for tc in range(T):
#     N = int(inputs())
#     students = [0]
#     students.extend(list(map(int, inputs().split())))
#     visited = [0]*(N+1)
#     team_num = 0
#
#     for start in range(1, N+1):
#         if visited[start] == 0:
#             trg, team = dfs(start)
#             if trg:
#                 team_num += len(team)
#                 for t in team:
#                     visited[t] = 1
#             elif not trg and visited[start] == 0:
#                 visited[start] = 1
#
#     print(N-team_num)


# v5
import sys

def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = 1
    visited_tmp = []
    visited_tmp.append(start)
    trg_tmp = False

    while stack:
        people = stack.pop()
        choice = students[people]
        if visited[choice] == 1:
            if choice in visited_tmp:
                trg_tmp = True
                visited_tmp = visited_tmp[visited_tmp.index(choice):]
            break
        if visited[choice] == 0:
            stack.append(choice)
            visited_tmp.append(choice)
            visited[choice] = 1
    return trg_tmp, visited_tmp

inputs = sys.stdin.readline

T = int(inputs())
for tc in range(T):
    N = int(inputs())
    students = [0]
    students.extend(list(map(int, inputs().split())))
    visited = [0]*(N+1)
    team_num = 0

    for start in range(1, N+1):
        if visited[start] == 0:
            trg, team = dfs(start)
            if trg:
                team_num += len(team)

    print(N-team_num)