# baekjoon_14501 퇴사
import sys

def time_dfs(time_pi,idx):
    stack = []
    stack.append(time_pi)
    # idx = timetable.index(time_pi)
    sum_pi = 0

    # v1
    # while stack:
    #     ti, pi = stack.pop()
    #     idx += ti
    #     if idx > N:
    #         break
    #     if (idx-1) < N:
    #         sum_pi += pi
    #         stack.append(timetable[idx])
    # return sum_pi

    # v2
    # while stack:
    #     ti, pi = stack.pop()
    #     idx += ti
    #     if (idx-1) < N:
    #         sum_pi += pi
    #     if idx >= N:
    #         break
    #     else:
    #         stack.append(timetable[idx])
    # return sum_pi

    # v3
    while stack:
        ti, pi = stack.pop()
        idx += ti
        if idx < N:
            sum_pi += pi
        if idx >= N:
            return sum_pi
        else:
            stack.append(timetable[idx])


N = int(input())
timetable = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

max_pi = 0
idx = 0
for time_pi in timetable:
    pi_tmp = time_dfs(time_pi, idx)
    idx += 1
    if pi_tmp > max_pi:
        max_pi = pi_tmp

print(max_pi)


