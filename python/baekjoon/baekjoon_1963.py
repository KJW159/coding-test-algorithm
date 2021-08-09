# baekjoon_1963 소수 경로

# v1
# from math import sqrt
#
#
# def is_prime_number(x):
#     for i in range(2, int(sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True
#
#
# def bfs():
#     for n1 in range(1, 10):
#         for n2 in range(0, 10):
#             for n3 in range(0, 10):
#                 for n4 in range(0, 10):
#
#
#
# T = int(input())
# A, B = map(int, input().split())
# visited = [0 for _ in range(10000)]
# visited[A] = 1
#
# bfs()


# v2
from math import sqrt
from collections import deque


def bfs(start, end):
    queue = deque()
    queue.append([start, 0])
    visited[start] = 1

    while queue:
        num, cnt = queue.popleft()
        if num == end:
            return cnt
        num_str = str(num)

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                j_tmp = str(j)
                num_changed = int(num_str[:i] + j_tmp + num_str[i+1:])
                if prime_nums[num_changed] == 1 and visited[num_changed] == 0:
                    queue.append([num_changed, cnt+1])
                    visited[num_changed] = 1
    return -1




T = int(input())
prime_nums = [1] * 10001


for i in range(2, int(sqrt(10000))+1):
    if prime_nums[i]:
        j = 2
        while i * j < 10000:
            if prime_nums[i*j]:
                prime_nums[i*j] = 0
            j += 1

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10001
    res = bfs(A, B)

    if res == -1:
        print("Impossible")
    else:
        print(res)