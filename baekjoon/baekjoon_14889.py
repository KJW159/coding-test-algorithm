# baekjoon_14889 스타트와 링크

# v1
# import math
#
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
# def checking_ability(arr):
#     score = 0
#     for members in combinations1(arr, 2):
#         m1, m2 = members
#         score += (company[m1][m2]+company[m2][m1])
#
#     return score
#
# N = int(input())
# company = [list(map(int, input().split())) for _ in range(N)]
#
# start_team = []
# link_team = []
# res = math.inf
# people = list(range(N))
#
# for team in combinations1(people, N // 2):
#     if team not in link_team:
#         start_team.append(team)
#         team_tmp = []
#         for member in range(N):
#             if member not in team:
#                 team_tmp.append(member)
#         link_team.append(team_tmp)
#
# for i in range(len(start_team)):
#     start_score = checking_ability(start_team[i])
#     link_score = checking_ability(link_team[i])
#     res = min(res, abs(start_score-link_score))
#
# print(res)


# v2
# import math
#
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
# def checking_ability(arr):
#     score = 0
#     for members in combinations1(arr, 2):
#         m1, m2 = members
#         score += (company[m1][m2]+company[m2][m1])
#
#     return score
#
# N = int(input())
# company = [list(map(int, input().split())) for _ in range(N)]
#
# start_team = []
# link_team = []
# res = math.inf
#
# for team in combinations1(list(range(N)), N // 2):
#     if team not in link_team:
#         start_team.append(team)
#     team = set(team)
#     people = set(range(N))
#     team_tmp = list(people - team)
#     link_team.append(team_tmp)
#
# for i in range(len(start_team)):
#     start_score = checking_ability(start_team[i])
#     link_score = checking_ability(link_team[i])
#     res = min(res, abs(start_score-link_score))
#
# print(res)

# v3
import math

def combinations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations1(arr[i+1:], r-1):
                yield [arr[i]] + next

def checking_ability(arr):
    score = 0
    for members in combinations1(arr, 2):
        m1, m2 = members
        score += (company[m1][m2]+company[m2][m1])

    return score

N = int(input())
company = [list(map(int, input().split())) for _ in range(N)]

res = math.inf
people = set(range(N))
for start_team in combinations1(list(range(N)), N // 2):
    start_score = checking_ability(start_team)
    start_team = set(start_team)
    link_team = list(people - start_team)
    link_score = checking_ability(link_team)
    res = min(res, abs(start_score - link_score))

print(res)