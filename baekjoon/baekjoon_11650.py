# baekjoon_11650

N = int(input())
coordinates = [tuple(map(int, input().split())) for k in range(N)]
coordinates = sorted(coordinates)
for x, y in coordinates:
    print(f'{x} {y}')