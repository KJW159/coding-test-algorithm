# baekjoon_10952

while True:
    A, B = list(map(int, input().split()))
    result = 0
    if A == 0 and B == 0:
        break
    result = A + B
    print(f'{result}')