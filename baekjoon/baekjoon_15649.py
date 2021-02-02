# baekjoon_15649 N과 M(1)

def permutations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations1(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next



N, M = map(int, input().split())
nums = []

for num in range(1, N+1):
    nums.append(num)

for permu in permutations1(nums, M):
    print(*permu)