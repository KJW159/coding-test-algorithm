# baekjoon 1330 두 수 비교하기.

num = int(input())
score = None

if 90 <= num <= 100:
    score = 'A'
elif 80 <= num < 90:
    score = 'B'
elif 70 <= num < 80:
    score = 'C'
elif 60 <= num < 70:
    score = 'D'
else:
    score = 'F'

print(score)

