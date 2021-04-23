# baekjoon_20058 마법사 상어와 파이어스톰

# v1
# def melting(s_i, s_j, K):
#     cnt = 0
#     trg = False
#     for c in range(4):
#         nx = s_i + dx[c]
#         ny = s_j + dy[c]
#         if 0 <= nx < K and 0 <= ny < K:
#             if arr[nx][ny]:
#                 cnt += 1
#         if cnt == 3:
#             trg = True
#             break
#     return trg
#
# def finding_ice(s_i, s_j, K):
#     stack = []
#     visited[s_i][s_j] = 1
#     stack.append([s_i,s_j])
#     cnt_tmp = 1
#     while stack:
#         s_i, s_j = stack.pop()
#         for c in range(4):
#             nx = s_i + dx[c]
#             ny = s_j + dy[c]
#             if 0 <= nx < K and 0 <= ny < K:
#                 if visited[nx][ny] == 0 and arr[nx][ny] !=0:
#                     cnt_tmp += 1
#                     stack.append([nx,ny])
#                     visited[nx][ny] = 1
#     return cnt_tmp
#
#
#
# N, Q = map(int, input().split())
# K = 2**N
# arr = [list(map(int, input().split())) for _ in range(K)]
# steps = list(map(int, input().split()))
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# visited = [[0]*K for _ in range(K)]
#
# for L in steps:
#     p = 2**L
#     for x in range(0,K,p):
#         for y in range(0,K,p):
#             tmp = [arr[i][y:y+p] for i in range(x,x+p)]
#             for i in range(p):
#                 for j in range(p):
#                     arr[x+j][y+p-1-i] = tmp[i][j]
#
#     melting_ice = []
#     for i in range(K):
#         for j in range(K):
#             if not melting(i,j,K):
#                 melting_ice.append([i,j])
#
#     for i_x, i_y in melting_ice:
#         if arr[i_x][i_y]:
#             arr[i_x][i_y] -= 1
#
# total_ice = 0
# area = 0
# for i in range(K):
#     for j in range(K):
#         total_ice += arr[i][j]
#         if visited[i][j] == 0 and arr[i][j] !=0:
#             area = max(area, finding_ice(i,j,K))
# print(total_ice)
# print(area)


# v2
# from collections import deque
#
# def melting(s_i, s_j, K):
#     cnt = 0
#     trg = False
#     for c in range(4):
#         nx = s_i + dx[c]
#         ny = s_j + dy[c]
#         if 0 <= nx < K and 0 <= ny < K:
#             if arr[nx][ny]:
#                 cnt += 1
#         if cnt == 3:
#             trg = True
#             break
#     return trg
#
# def finding_ice(s_i, s_j, K):
#     queue = deque()
#     visited[s_i][s_j] = 1
#     queue.append([s_i,s_j])
#     cnt_tmp = 1
#     while queue:
#         s_i, s_j = queue.popleft()
#         for c in range(4):
#             nx = s_i + dx[c]
#             ny = s_j + dy[c]
#             if 0 <= nx < K and 0 <= ny < K:
#                 if visited[nx][ny] == 0 and arr[nx][ny] !=0:
#                     cnt_tmp += 1
#                     queue.append([nx,ny])
#                     visited[nx][ny] = 1
#     return cnt_tmp
#
#
#
# N, Q = map(int, input().split())
# K = 2**N
# arr = [list(map(int, input().split())) for _ in range(K)]
# steps = list(map(int, input().split()))
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
# visited = [[0]*K for _ in range(K)]
#
# for L in steps:
#     p = 2**L
#     for x in range(0,K,p):
#         for y in range(0,K,p):
#             tmp = [arr[i][y:y+p] for i in range(x,x+p)]
#             for i in range(p):
#                 for j in range(p):
#                     arr[x+j][y+p-1-i] = tmp[i][j]
#
#     melting_ice = []
#     for i in range(K):
#         for j in range(K):
#             if not melting(i,j,K):
#                 melting_ice.append([i,j])
#
#     for i_x, i_y in melting_ice:
#         if arr[i_x][i_y]:
#             arr[i_x][i_y] -= 1
#
# total_ice = 0
# area = 0
# for i in range(K):
#     for j in range(K):
#         total_ice += arr[i][j]
#         if visited[i][j] == 0 and arr[i][j]:
#             area = max(area, finding_ice(i,j,K))
# print(total_ice)
# print(area)



# re-v1
# from collections import deque
#
# def checking(i,j,size):
#     cnt = 0
#
#     for c in range(4):
#         x = i + dx[c]
#         y = j + dy[c]
#         if 0 <= x < size and 0 <= y < size:
#             if arr[x][y] != 0:
#                 cnt += 1
#         if cnt == 3:
#             return False
#     return True
#
#
# def bfs(i,j, size):
#     queue = deque()
#     queue.append([i,j])
#     visited[i][j] = 1
#
#     area_cnt = 1
#     ices_num = arr[i][j]
#
#     while queue:
#         i, j = queue.popleft()
#         for c in range(4):
#             x = i + dx[c]
#             y = j + dy[c]
#             if 0 <= x < size and 0 <= y < size:
#                 if arr[x][y] != 0 and visited[x][y] == 0:
#                     queue.append([x,y])
#                     visited[x][y] = 1
#                     ices_num += arr[x][y]
#                     area_cnt += 1
#     return ices_num, area_cnt
#
#
#
#
# N, Q = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(2**N)]
# magic_steps = list(map(int, input().split()))
#
# size = 2**N
#
# dx = [0,-1,0,1]
# dy = [-1,0,1,0]
#
# for q in range(Q):
#     L = magic_steps[q]
#     # 격자 나누기
#     p = 2**L
#     for i in range(0,size,p):
#         for j in range(0,size,p):
#             tmp = [arr[c][j:j+p] for c in range(i,i+p)]
#             # 격자 돌리기
#             for x in range(p):
#                 for y in range(p):
#                     arr[i+y][j+p-1-x] = tmp[x][y]
#
#     melting_ices = []
#     for i in range(size):
#         for j in range(size):
#             if arr[i][j] != 0:
#                 if checking(i,j,size):
#                     melting_ices.append([i,j])
#
#     for i, j in melting_ices:
#         if arr[i][j] != 0:
#             arr[i][j] -= 1
#
# left_ices = 0
# max_area = 0
# visited = [[0]*size for _ in range(size)]
# for i in range(size):
#     for j in range(size):
#         if arr[i][j] and visited[i][j] == 0:
#             ices_tmp = bfs(i,j,size)
#             left_ices += ices_tmp[0]
#             max_area = max(max_area, ices_tmp[1])
# print(left_ices)
# print(max_area)



# 조건
#  2^N 격자, 얼음양 의미.
# L단계면 2^L 격자로 나눔.
# 시계방향 90도로 회전
# 주변에 얼음있는 칸이 3칸 이상 없으면 -1
# Q번 시행,
# 남아있는 얼음 합, 가장 큰 덩어리가 차지하는 칸의 개수



# 풀이
# 격자 나누기 + 회전
    # 0부터 2^N까지 2^L 만큼 for을 돌면서 시작점을 옮겨줌.
    # 시작점에서 2^L 만큼 돌면서 복사와 함께 회전시킨 위치에 임시 공간에 담음.
    # 임시 공간에 있는 것을 원복에 덮어 씌움.
# 이중 for문으로 탐색 하면서 상하좌우 체크하고 녹일 좌표를 가져온다음.
# 좌표 꺼내면서 녹임.
# Q 번 시행한 이후에 2중 for문 써서 탐색하는데 방문 안하고 얼음 있으면 bfs들어감.
# bfs 돌면서 덩어리 칸 수 새어주고, max 비교 해줌.


# re-v2
import sys
from collections import deque


def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1

    cnt=1
    ice_cnt = 0

    while queue:
        i, j = queue.popleft()
        for c in range(4):
            x = i + dx[c]
            y = j + dy[c]
            if 0 <= x < R and 0 <= y < R:
                if ice[x][y] > 0 and visited[x][y] == 0:
                    queue.append([x,y])
                    visited[x][y] = 1
                    cnt += 1
                    ice_cnt += ice[x][y]
    return cnt, ice_cnt
input = sys.stdin.readline
N, Q = map(int, input().split())
R = 2**N
ice = [list(map(int, input().split())) for _ in range(R)]
steps = list(map(int, input().split()))

dx = [0,-1,0,1]
dy = [-1,0,1,0]


for L in steps:
    L2 = 2**L
    for i in range(0,R,L2):
        for j in range(0,R,L2):
            ice_tmp = [[0]*L2 for _ in range(L2)]
            for x in range(L2):
                for y in range(L2):
                    ice_tmp[y][L2-1-x] = ice[i+x][j+y]
            for x in range(L2):
                for y in range(L2):
                    ice[i+x][j+y] = ice_tmp[x][y]
    melting_ices = []
    for i in range(R):
        for j in range(R):
            cnt = 0
            for c in range(4):
                x = i + dx[c]
                y = j + dy[c]
                if 0 <= x < R and 0 <= y < R:
                    if ice[x][y] > 0:
                        cnt += 1
                if cnt == 3:
                    break
            if cnt !=3:
                melting_ices.append([i,j])
    for i_x, i_y in melting_ices:
        ice[i_x][i_y] -= 1


visited = [[0]*R for _ in range(R)]
total_ice = 0
max_land = 0
for i in range(R):
    for j in range(R):
        if ice[i][j] > 0 and visited[i][j] == 0:
            total_ice += ice[i][j]
            land_size , ice_cnt = bfs(i,j)
            total_ice += ice_cnt
            max_land = max(max_land, land_size)
print(total_ice)
print(max_land)



