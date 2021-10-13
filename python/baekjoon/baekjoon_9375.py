# baekjoon_9375 패션왕 신해빈

# v1
from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    clothes = defaultdict(int)
    for i in range(N):
        a, b = input().split()
        clothes[b] += 1

    res = 1
    for key in clothes:
        res *= (clothes[key]+1)
    print(res-1)