# baekjoon_17281 야구

# v1
# from itertools import permutations
# from collections import deque
#
#
# def playing_game(team):
#     out_cnt = 0
#     score_tmp = 0
#     field = deque([0,0,0,0])
#     p = -1
#     while True:
#         p += 1
#         p = p % 9
#         play = score[team[p]]
#         if play == 0:
#             out_cnt += 1
#             if out_cnt == 3:
#                 last_player = p
#                 return score_tmp, last_player
#         if 0 < play <=3:
#             field.rotate(play)
#             field[0] = 1
#             if field[3] == 1:
#                 score_tmp += 1
#                 field[3] = 0
#         if play == 4:
#             score_tmp += (sum(field)+1)
#             field = deque([0,0,0,0])

# N = int(input())
# res = 0
# start_player_tmp = 0
# for i in range(N):
#     score = list(map(int, input().split()))
#     score_max = 0
#     players = list(range(0, 9))
#     start_player = start_player_tmp
#     if i == 0:
#         start_player = 0
#     players.pop(start_player)
#     for team in permutations(players):
#         team = list(team)
#         if i == 0:
#             team.insert(3, 0)
#         if i > 0:
#             team.insert(0, start_player)
#         score_tmp, last_player = playing_game(team)
#         if score_max < score_tmp:
#             score_max = score_tmp
#             start_player_tmp = (last_player + 1) % 9
#     res += score_max
#
# print(res)


# v2
# from itertools import permutations
# from collections import deque
#
#
# def playing_game(team, score, start_player):
#     out_cnt = 0
#     score_tmp = 0
#     field = deque([0,0,0,0,0])
#     while True:
#         start_player = (start_player+1) % 9
#         play = score[team[start_player]]
#         if play == 0:
#             out_cnt += 1
#             if out_cnt == 3:
#                 last_player = start_player
#                 return score_tmp, last_player
#         if 0 < play <= 3:
#             field[0] = 1
#             for j in range(play):
#                 field.rotate(1)
#                 if field[4] == 1:
#                     score_tmp += 1
#                     field[4] = 0
#         if play == 4:
#             score_tmp += (sum(field)+1)
#             field = deque([0,0,0,0,0])
#
# N = int(input())
# res = 0
# start_player_tmp = 0
# scores = [list(map(int, input().split())) for _ in range(N)]
# players = list(range(1, 9))
# for team in permutations(players):
#     team = list(team)
#     team.insert(3, 0)
#     score_max = 0
#     last_player = -1
#     for i in range(N):
#         score = scores[i]
#         score_tmp, last_player = playing_game(team, score, last_player)
#         score_max += score_tmp
#     res = max(res, score_max)
#
# print(res)

# v3
from itertools import permutations

def playing_game(team, score, start_player):
    out_cnt = 0
    score_tmp = 0
    b1, b2, b3 = 0, 0, 0
    while True:
        start_player = (start_player+1) % 9
        play = score[team[start_player]]
        if play == 0:
            out_cnt += 1
            if out_cnt == 3:
                last_player = start_player
                return score_tmp, last_player
        if play == 1:
            score_tmp += b3
            b1, b2, b3 = 1, b1, b2
        if play == 2:
            score_tmp += (b2 + b3)
            b1, b2, b3 = 0,1,b1
        if play == 3:
            score_tmp += (b1 + b2 + b3)
            b1, b2, b3 = 0, 0, 1
        if play == 4:
            score_tmp += (b1 + b2 + b3 + 1)
            b1, b2, b3, = 0, 0, 0

N = int(input())
res = 0
start_player_tmp = 0
scores = [list(map(int, input().split())) for _ in range(N)]
players = list(range(1, 9))
for team in permutations(players):
    team = list(team)
    team.insert(3, 0)
    score_max = 0
    last_player = -1
    for i in range(N):
        score = scores[i]
        score_tmp, last_player = playing_game(team, score, last_player)
        score_max += score_tmp
    res = max(res, score_max)

print(res)