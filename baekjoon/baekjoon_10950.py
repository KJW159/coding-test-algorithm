# baekjoon_10950 A+B-3

T = int(input())

for tc in range(T):
    result = 0
    A, B = list(map(int, input().split()))
    result = A + B
    print('{}'.format(result))