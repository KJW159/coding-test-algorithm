# baekjoon_11659 구간 합 구하기 4


# v1
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]*(N+1)
num_sum = 0

for i in range(N):
    num_sum += nums[i]
    prefix_sum[i+1] = num_sum


for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b]-prefix_sum[a-1])