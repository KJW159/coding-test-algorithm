# baekjoon_10773 제로

N = int(input())

arr = [int(input()) for n in range(N)]

stack = []
for num in arr:
    if num == 0:
        if stack:
            stack.pop()
        else:
            pass
    elif num > 0:
        stack.append(num)
result = sum(stack)
print(f'{result}')
