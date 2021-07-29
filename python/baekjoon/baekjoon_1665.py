# baekjoon_1665 가운데를 말해요

# v1
import heapq
import sys

input = sys.stdin.readline

N = int(input())
max_hq = []
min_hq = []

middle_nums = []

for i in range(N):
    num = int(input())
    if len(max_hq) == len(min_hq):
        heapq.heappush(max_hq, -num)
    else:
        heapq.heappush(min_hq, num)

    if len(max_hq) >= 1 and len(min_hq) >= 1 and -max_hq[0] > min_hq[0]:
        max_num = -heapq.heappop(max_hq)
        min_num = heapq.heappop(min_hq)
        heapq.heappush(min_hq, max_num)
        heapq.heappush(max_hq, -min_num)
    print(-max_hq[0])
