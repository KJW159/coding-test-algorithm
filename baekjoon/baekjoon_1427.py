# baekjoon_1427 소트인사이드

N = str(input())
nums = []
number = ''
for num in N:
    nums.append(int(num))
nums.sort(reverse=True)

for num in nums:
    number += str(num)
print(number)
