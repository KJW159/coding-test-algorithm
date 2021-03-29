# baekjoon_15651 N과 M(3)

def product1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product1(arr[:], r-1):
                yield [arr[i]] + next



N, M = map(int, input().split())
nums = []
for num in range(1, N+1):
    nums.append(num)

for pro in product1(nums, M):
    print(*pro)