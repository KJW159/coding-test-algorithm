# baekjoon_10871

N, X = list(map(int, input().split()))
nums = list(map(int, input().split()))
result = []
for num in nums:
    if num < X:
        result.append(num)

for num_res in result:
    print(f'{num_res}', end=' ')
