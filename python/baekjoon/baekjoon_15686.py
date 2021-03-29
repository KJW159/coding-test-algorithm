# baekjoon_15686 치킨 배달

# v1
# import math
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r ==1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# N, M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
#
# houses = []
# chickens = []
# res = math.inf
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 1:
#             houses.append([i,j])
#         if city[i][j] == 2:
#             chickens.append([i,j])
#
# for stores in combinations1(chickens, M):
#     city_dist = 0
#     for house in houses:
#         chick_dist = math.inf
#         h_i, h_j = house
#         for store in stores:
#             s_i, s_j = store
#             dist_tmp = abs(h_i-s_i)+abs(h_j-s_j)
#             chick_dist = min(chick_dist, dist_tmp)
#         city_dist += chick_dist
#     res = min(res, city_dist)
# print(res)


# v2
import math
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
res = math.inf
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i,j])
        if city[i][j] == 2:
            chickens.append([i,j])

for stores in combinations(chickens, M):
    city_dist = 0
    for house in houses:
        chick_dist = math.inf
        h_i, h_j = house
        for store in stores:
            s_i, s_j = store
            dist_tmp = abs(h_i-s_i)+abs(h_j-s_j)
            chick_dist = min(chick_dist, dist_tmp)
        city_dist += chick_dist
    res = min(res, city_dist)
print(res)