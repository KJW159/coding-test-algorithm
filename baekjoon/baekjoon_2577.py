#backjoon_2557 숫자의 개수

nums = [int(input()) for i in range(3)]

num = nums[0] * nums[1] * nums[2]
num = str(num)
for j in range(10):
    result = 0
    j = str(j)
    result = num.count(j)
    print(f'{result}')
