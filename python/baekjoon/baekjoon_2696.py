# baekjoon_2696 중앙값 구하기

# v1
import heapq


T = int(input())
for tc in range(T):
    M = int(input())
    nums = list(map(int, input().split()))
    max_hq = []
    min_hq = []

    middle_nums = []

    for i in range(1, M+1):
        if i % 2 == 1:
            heapq.heappush(min_hq, nums[i])
        else:
            heapq.heappush(max_hq, -nums[i])

        if i % 2 == 1:
            if i > 1:
                if -max_hq[0] > min_hq[0]:
                    max_num = -heapq.heappop(max_hq)
                    min_num = heapq.heappop(min_hq)
                    heapq.heappush(min_hq, max_num)
                    heapq.heappush(max_hq, -min_num)

            else:
                middle_nums.append(min_hq[0])
    print(middle_nums)
