# baekjoon_3052 나머지

N = 10
nums = [int(input()) for n in range(N)]
result = []
for num in nums:
    remainder = num % 42
    if not(remainder in result):
        result.append(remainder)
print(f'{len(result)}')