# baekjoon_1158 요세푸스 문제

# v1
# from collections import deque
#
# N, K = map(int,input().split())
# queue = deque()
# for i in range(1, N+1):
#     queue.append(i)
#
# res = []
# while queue:
#     queue.rotate(-(K-1))
#     num = queue.popleft()
#     res.append(num)
# print("<", end="")
# for i in range(N-1):
#     print("{}, ".format(res[i]), end="")
# print("{}".format(res[N-1]), end="")
# print(">")


# v2
from collections import deque

N, K = map(int,input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

res = []
while queue:
    queue.rotate(-(K-1))
    num = queue.popleft()
    res.append(str(num))
print("{}{}{}".format("<",", ".join(res),">"))