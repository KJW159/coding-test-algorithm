# baekjoon_9184 신나는 함수 실행

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b and b < c:
        if dp[a][b][c-1] != 0 and dp[a][b-1][c-1] !=0 and dp[a][b-1][c] !=0:
            return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
        else:
            dp[a][b][c - 1] = w(a, b, c-1)
            dp[a][b - 1][c - 1] = w(a, b-1, c-1)
            dp[a][b - 1][c] = w(a, b-1, c)
            return dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c]
    else:
        if dp[a-1][b][c] != 0 and dp[a-1][b - 1][c] != 0 and dp[a-1][b][c-1] != 0 and dp[a-1][b-1][c-1]:
            return dp[a-1][b][c] + dp[a-1][b - 1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
        else:
            dp[a - 1][b][c] = w(a-1, b, c)
            dp[a - 1][b - 1][c] = w(a-1, b-1, c)
            dp[a - 1][b][c - 1] = w(a-1, b, c-1)
            dp[a - 1][b - 1][c - 1] = w(a-1, b-1, c-1)
            return dp[a-1][b][c] + dp[a-1][b - 1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]


while True:
    a, b, c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    dp = [[[0]*21 for _ in range(21)] for __ in range(21)]
    result = w(a, b, c)
    print("w({}, {}, {}) = {}".format(a, b, c, result))
