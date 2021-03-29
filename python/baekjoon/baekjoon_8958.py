# baekjoon_8958 ox퀴즈

T = int(input())

for tc in range(T):
    quizs = input()
    score = 0
    cnt_tmp = 0
    for quiz in quizs:
        if quiz == 'O':
            cnt_tmp += 1
            score += cnt_tmp
        else:
            cnt_tmp = 0

    print(f'{score}')