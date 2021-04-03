
#v1
# from collections import deque
#
# def solution(progresses, speeds):
#     answer = []
#     deq = deque()
#     for i in range(len(speeds)):
#         deq.append([progresses[i], speeds[i]])
#
#     while deq:
#         cnt = 0
#         for i in range(len(deq)):
#             deq[i][0] += deq[i][1]
#         if deq[0][0] >= 100:
#             for i in range(len(deq)):
#                 if deq[i][0] >= 100:
#                     cnt += 1
#                 else:
#                     break
#             for j in range(cnt):
#                 deq.popleft()
#         if cnt > 0:
#             answer.append(cnt)
#
#     return answer



# v2
def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt = 0
        work_num = len(progresses)
        for i in range(work_num):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            for i in range(work_num):
                if progresses[i] >= 100:
                    cnt += 1
                else:
                    break
            for j in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
        if cnt > 0:
            answer.append(cnt)

    return answer

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solution(a,b))