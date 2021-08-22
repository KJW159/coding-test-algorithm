# baekjoon_3015 오아시스 재결합

# v1
N = int(input())
stack = []
res = 0

for _ in range(N):
    new_num = int(input())
    cnt = 1
    while stack:
        if stack[-1][0] < new_num:
            res += stack.pop()[1]
            cnt = 1
        elif stack[-1][0] == new_num:
            cnt = stack.pop()[1]
            res += cnt
            cnt += 1
        else:
            res += 1
            break
    stack.append([new_num, cnt])
print(res)


