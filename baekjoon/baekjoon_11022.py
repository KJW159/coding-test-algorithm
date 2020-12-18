# baekjoon 11022 A+B -8

T = int(input())

for tc in range(1, T+1):
    result = 0
    A, B = list(map(int, input().split()))
    result = A + B
    print(f'Case #{tc}: {A} + {B} = {result}')