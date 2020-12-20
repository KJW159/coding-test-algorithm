# baekjoon_1110 더하기 사이클

N = int(input())
cnt = 0
result = 0
new_num = N
while True:
    if new_num < 10:
        N_10 = 0
        N_1 = new_num
    else:
        N_10 = new_num // 10
        N_1 = new_num % 10
    tmp = N_10 + N_1
    new_num = N_1 * 10 + tmp % 10
    if new_num == N:
        cnt += 1
        result = cnt
        break
    else:
        cnt += 1
print(f'{result}')







