# baekjoon_10818

T = int(input())
nums = list(map(int, input().split()))

min = 10000000
max = -10000000
for num in nums:
    if num < min:
        min = num
    if num > max:
        max = num

print(f'{min} {max}')
