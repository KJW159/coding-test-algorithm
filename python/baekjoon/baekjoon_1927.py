# baekjoon_11279 최대 힙


#v1
# import heapq
#
# N = int(input())
# heap = []
# for _ in range(N):
#     num = int(input())
#     if num == 0:
#         if heap:
#             print(heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, num)

# v2
import heapq
import sys

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)

