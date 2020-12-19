# baekjoon_7568 덩치

N = int(input())

people = [list(map(int, input().split())) for n in range(N)]
ranking = []

for i in range(N):
    man1_w = people[i][0]
    man1_h = people[i][1]
    rank = 1
    for j in range(N):
        man2_w = people[j][0]
        man2_h = people[j][1]
        if man1_h < man2_h and man1_w < man2_w:
            rank += 1
    ranking.append(rank)

for k in ranking:
    print(f'{k}', end=' ')


