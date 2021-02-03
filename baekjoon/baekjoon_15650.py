# baekjoon_15650 N과 M(2)

def combinations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations1(arr[i+1:], r-1):
                yield [arr[i]] + next



N, M = map(int, input().split())
nums = []
for num in range(1, N+1):
    nums.append(num)

for comb in combinations1(nums, M):
    print(*comb)