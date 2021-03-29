# baekjoon_11279 최대 힙

# v1
# import sys
# import heapq
#
# N = int(input())
# heap_max = []
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         if heap_max:
#             print(heapq.heappop(heap_max)[1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap_max, (-num, num))


# v2
import sys
import heapq

N = int(input())
heap_max = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap_max:
            print(-heapq.heappop(heap_max))
        else:
            print(0)
    else:
        heapq.heappush(heap_max, -num)