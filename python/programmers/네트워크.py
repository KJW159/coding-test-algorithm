
# v1
# def dfs(i):
#     stack = []
#     visited[i] = 1
#     stack.append(i)
#
#     while stack:
#         i = stack.pop()
#         idx = 0
#         for j in computers[i]:
#             if visited[idx] == 0 and j == 1:
#                 stack.append(idx)
#                 visited[idx] = 1
#             idx += 1
#
# def solution(n, computers):
#     global visited
#     visited = [0]*n
#     cnt = 0
#     for i in range(n):
#         if visited[i] == 0:
#             dfs(i)
#             cnt += 1
#
#     answer = cnt
#     return answer


# v2


def solution(n, computers):
    visited = [0]*n
    def dfs(i):
        stack = []
        visited[i] = 1
        stack.append(i)

        while stack:
            i = stack.pop()
            for j in range(len(computers[i])):
                if visited[j] == 0 and computers[i][j] == 1:
                    stack.append(j)
                    visited[j] = 1
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            cnt += 1

    answer = cnt
    return answer
n = int(input())
computers = [list(map(int, input().split(','))) for _ in range(n)]
print(solution(n, computers))