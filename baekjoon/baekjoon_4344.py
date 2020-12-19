# baekjoon_4344 평균은 넘겠지

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    stud_num = nums[0]
    scores = nums[1:]
    sum_s = sum(scores)
    mean_s = sum_s / stud_num
    cnt = 0
    for score in scores:
        if score > mean_s:
            cnt += 1
    result = round((cnt/stud_num)*100, 3)
    print(f'{result:.3f}%')