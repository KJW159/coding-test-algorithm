# baekjoon_2493 탑

# v1
# N = int(input())
# towers = list(map(int, input().split()))
# res = [0]*N
#
# for i in range(N-1, 0, -1):
#     for j in range(i-1, -1, -1):
#         if towers[j] >= towers[i]:
#             res[i] = j+1
#             break
# print(*res)


# v2

N = int(input())
towers = list(map(int, input().split()))
res = [0]
stack = []
stack.append([0, towers[0]])

for i in range(1, N):
    while stack:
        if stack[-1][1] >= towers[i]:
            res.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        res.append(0)
    stack.append([i, towers[i]])
print(*res)