# baekjoon_2562 최댓값

N = 9
max_num = 0
cnt = 0
for i in range(N):
    cnt += 1
    num = int(input())
    if num > max_num:
        max_num = num
        cnt_res = cnt
print(f'{max_num}')
print(f'{cnt_res}')
