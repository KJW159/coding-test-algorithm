# baekjoon_2750 수 정렬하기

N = int(input())

nums = [int(input()) for k in range(N)]
nums.sort()
for num in nums:
    print(f'{num}')