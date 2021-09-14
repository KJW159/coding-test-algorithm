# baekjoon_11441 합 구하기

# v1
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
prefix_sum = [0]*(N+1)

sum_tmp = 0
for i in range(N):
    sum_tmp += nums[i]
    prefix_sum[i+1] = sum_tmp

M = int(input())
for _ in range(M):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left-1])