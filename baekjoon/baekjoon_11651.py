#baekjoon_11651 좌표 정렬하기2

N = int(input())
coordinates = [tuple(map(int, input().split())) for n in range(N)]
coordinates = sorted(coordinates, key=lambda x : (x[1], x[0]))
for x, y in coordinates:
    print(f'{x} {y}')
