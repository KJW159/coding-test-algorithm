# baekjoon_10814 나이순 정렬

N = int(input())

members = enumerate([list(input().split()) for n in range(N)])
members = sorted(members, key=lambda x : (int(x[1][0]),x[0]))
for idx, member in members:
    print(f'{member[0]} {member[1]}')