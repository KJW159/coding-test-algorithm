from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i], i])
    cnt = 0
    while True:
        max_pri = 0
        for i in range(len(queue)):
            max_pri = max(queue[i][0], max_pri)
        priority, position = queue.popleft()
        if priority == max_pri:
            cnt += 1
            if position == location:
                answer = cnt
                break
        if priority < max_pri:
            queue.append([priority, position])

    return answer