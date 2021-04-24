# swea_2070 큰놈, 작은놈, 같은 놈

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    n1, n2 = map(int, input().split())
    res = ''
    if n1 > n2:
        res = '>'
    elif n1 == n2:
        res = '='
    elif n1 < n2 :
        res = '<'

    print("#{} {}".format(tc, res))


