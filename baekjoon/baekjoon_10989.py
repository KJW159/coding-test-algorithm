# baekjoon_10989 수 정렬하기3

N = int(input())

nums = [int(input()) for i in range(N)]
k = max(nums)
counts = [0]*(k+1)
tmp = [0]*N

for num in nums:
    counts[num] += 1

for i in range(len(counts)-1):
    counts[i+1] += counts[i]

for num in nums:
    tmp[counts[num]-1] = num
    counts[num] -= 1

for num in tmp:
    print(f'{num}')


