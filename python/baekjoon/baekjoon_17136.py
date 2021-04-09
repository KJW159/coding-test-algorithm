# baekjoon_17136 색종이 붙이기

# v1
# from collections import deque
# import math
#
#
# def finding_area(i,j):
#     queue = deque()
#     queue.append([i,j])
#     visited1[i][j] = 1
#     cnt = 1
#
#     while queue:
#         i, j = queue.popleft()
#         for c in range(4):
#             x = i + dx[c]
#             y = j + dy[c]
#             if 0 <= x < 10 and 0 <= y < 10:
#                 if papers[x][y] == 1 and visited1[x][y] == 0:
#                     queue.append([x,y])
#                     cnt += 1
#                     visited1[x][y] = 1
#     return cnt
#
#
# def covering_papers(total,colored_tmp, area_tmp):
#     global res
#     trg = True
#     for k in range(1, len(area_tmp)):
#         if area_tmp[k] > 0:
#             trg = False
#     if trg:
#         res = min(res, total)
#         return
#     if total == 0:
#         if area_tmp:
#             res = -1
#             return
#         else:
#             res = min(res, total)
#             return
#     for i in range(5, 0, -1):
#         if i**2 <= area_tmp[0] and colored_tmp[i] != 0:
#             area_tmp[0] -= i**2
#             colored_tmp[i] -= 1
#             covering_papers(total-1,colored_tmp, sorted(area_tmp, reverse=True))
#             area_tmp[0] += i**2
#             colored_tmp[i] += 1
#
#
#
# papers = [list(map(int, input().split())) for _ in range(10)]
# area = []
# colored_papers = [0]+[5]*5
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = math.inf
#
# visited1 = [[0]*10 for _ in range(10)]
# for i in range(10):
#     for j in range(10):
#         if papers[i][j] == 1 and visited1[i][j] == 0:
#             area.append(finding_area(i,j))
# covering_papers(25, colored_papers, area)
# print(25-res)



# v2

# def isCovered(i,j,k):
#     for x in range(i, i+k):
#         for y in range(j, j+k):
#             if 0 <= x < 10 and 0 <= y < 10:
#                 if papers[x][y] != 1:
#                     return False
#             else:
#                 return False
#     return True
#
#
# def covering_papers(cnt):
#     global res, total_area
#
#     if cnt >= res:
#         return
#
#     if total_area == 0:
#         res = min(res, cnt)
#         return
#
#     trg = False
#     s_i = 0
#     s_j = 0
#     for i in range(10):
#         if trg:
#             break
#         for j in range(10):
#             if papers[i][j] == 1:
#                 s_i = i
#                 s_j = j
#                 trg =True
#                 break
#
#
#     if papers[s_i][s_j] == 1:
#         for k in range(5, 0, -1):
#             if colored_papers[k]:
#                 covered = []
#                 if isCovered(s_i,s_j,k):
#                     for x in range(s_i, s_i+k):
#                         for y in range(s_j, s_j+k):
#                             papers[x][y] = 0
#                             covered.append([x,y])
#
#                     total_area -= k ** 2
#                     colored_papers[k] -= 1
#                     covering_papers(cnt+1)
#                     total_area += k ** 2
#                     colored_papers[k] += 1
#
#                     for nx, ny in covered:
#                         papers[nx][ny] = 1
#
#
#
# papers = [list(map(int, input().split())) for _ in range(10)]
# total_area = 0
# colored_papers = [0]+[5]*5
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# res = 26
#
# visited1 = [[0]*10 for _ in range(10)]
# for i in range(10):
#     for j in range(10):
#         if papers[i][j] == 1:
#             total_area += 1
# covering_papers(0)
# if res == 26:
#     print(-1)
# else:
#     print(res)


# v3

def isCovered(i,j,k):
    for x in range(i, i+k):
        for y in range(j, j+k):
            if 0 <= x < 10 and 0 <= y < 10:
                if papers[x][y] != 1:
                    return False
            else:
                return False
    return True


def changing_papers(s_i,s_j, k, val):
    for x in range(s_i, s_i+k):
        for y in range(s_j, s_j+k):
            papers[x][y] = val

def covering_papers(cnt):
    global res, total_area

    if cnt >= res:
        return

    if total_area == 0:
        res = min(res, cnt)
        return

    trg = False
    s_i = 0
    s_j = 0
    for i in range(10):
        if trg:
            break
        for j in range(10):
            if papers[i][j] == 1:
                s_i = i
                s_j = j
                trg =True
                break

    if papers[s_i][s_j] == 1:
        for k in range(5, 0, -1):
            if colored_papers[k] and isCovered(s_i,s_j,k):
                    changing_papers(s_i, s_j, k, 0)
                    total_area -= k ** 2
                    colored_papers[k] -= 1
                    covering_papers(cnt+1)
                    total_area += k ** 2
                    colored_papers[k] += 1
                    changing_papers(s_i, s_j, k, 1)


papers = [list(map(int, input().split())) for _ in range(10)]
total_area = 0
colored_papers = [0]+[5]*5
dx = [0,-1,0,1]
dy = [-1,0,1,0]
res = 26

visited1 = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if papers[i][j] == 1:
            total_area += 1
covering_papers(0)
if res == 26:
    print(-1)
else:
    print(res)