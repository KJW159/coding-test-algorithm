import collections

def chess_move(s_position, e_position):

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    cnt = 0
    queue = collections.deque()
    queue.append(s_position)
    chessboard[s_position[0]][s_position[1]] = 1

    while queue:
        i_x, j_y = queue.popleft()
        if i_x == e_position[0] and j_y == e_position[1]:
            cnt = chessboard[i_x][j_y]-1
            break

        for c in range(8):
            x = i_x + dx[c]
            y = j_y + dy[c]
            if 0 <= x < chessboard_length and 0 <= y < chessboard_length:
                if chessboard[x][y] == 0:
                    chessboard[x][y] = chessboard[i_x][j_y] + 1
                    queue.append([x, y])

    return cnt

T = int(input())

for tc in range(T):
    chessboard_length = int(input())
    if 4 <= chessboard_length <= 300:
        chessboard = [[0] * chessboard_length for _ in range(chessboard_length)]

        s_position = list(map(int, input().split()))
        e_position = list(map(int, input().split()))

        result = chess_move(s_position, e_position)
        print(result)
