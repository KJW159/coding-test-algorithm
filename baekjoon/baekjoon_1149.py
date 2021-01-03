# baekjoon_1149 RGB 거리


# v1
# N = int(input())
#
# color_cost = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*3 for __ in range(N)]
#
# dp[0][0] = color_cost[0][0]
# dp[0][1] = color_cost[0][1]
# dp[0][2] = color_cost[0][2]
#
# for i in range(N):
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color_cost[i][0]
#     dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color_cost[i][1]
#     dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color_cost[i][2]
# res = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
# print(res)


# v2

def cost_check(N):
    if N == 1:
        pass
    else:
        cost_check(N-1)






N = int(input())

color_cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for __ in range(N)]

dp[0][0] = color_cost[0][0]
dp[0][1] = color_cost[0][1]
dp[0][2] = color_cost[0][2]

res = cost_check()
print(res)


