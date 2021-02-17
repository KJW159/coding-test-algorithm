# baekjoon_14503 로봇청소기

def checking_left(r_i,r_j,direction, rotating):
    x = r_i + dx[direction]
    y = r_j + dy[direction]
    trg_tmp = False
    if 0 <= x < N and 0 <= y < M:
        if visited[x][y] == 0 and room[x][y] == 0:
            trg_tmp = True
    if direction-1 < 0:
        direction = 4
    return trg_tmp, [x ,y, direction, rotating]


def moving_backward(r_i, r_j, direction, rotating):
    move_tmp = False
    bx = 0
    by = 0
    if direction == 0:
        bx = r_i + dx[3]
        by = r_j + dy[3]
    elif direction == 1:
        bx = r_i + dx[0]
        by = r_j + dy[0]
    elif direction == 2:
        bx = r_i + dx[1]
        by = r_j + dy[1]
    elif direction == 3:
        bx = r_i + dx[2]
        by = r_j + dy[2]

    if 0 <= bx < N and 0 <= by < M:
        if room[bx][by] == 0:
            move_tmp = True
            return move_tmp, [bx, by, direction, rotating]
    return move_tmp, [r_i, r_j, direction, rotating]

N, M = map(int, input().split())
robot = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
rotating = 0
robot.append(rotating)

stack = []
stack.append(robot)
visited[robot[0]][robot[1]] = 1
clean_cnt = 1

# 해당 방향(인덱스)에 따른 탐색 방향
dx = [0,-1,0,1]
dy = [-1,0,1,0]


while stack:
    r_i, r_j, direction, rotating = stack.pop()
    clean, robot = checking_left(r_i, r_j, direction, rotating)
    if clean:
        robot[2] -= 1
        robot[3] = 0
        stack.append(robot)
        visited[robot[0]][robot[1]] = 1
        clean_cnt += 1
    if not clean and robot[3] < 4:
        rotating += 1
        if direction-1 < 0:
            direction = 4
        stack.append([r_i, r_j, direction-1, rotating])
    if not clean and robot[3] == 4:
        rotating = 0
        move, robot = moving_backward(r_i, r_j, direction, rotating)
        if move:
            stack.append(robot)
        else:
            break
print(clean_cnt)

