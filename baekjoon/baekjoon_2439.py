# baekjoon_2439 별 찍기 -2

N = int(input())

stars = ''
for n in range(N):
    stars += '*'

for i in range(N-1, -1, -1):
    star_edited = stars.replace('*', ' ', i)
    print(star_edited)

