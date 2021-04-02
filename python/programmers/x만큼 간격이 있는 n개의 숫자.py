def solution(x, n):
    answer = []
    if x == 0:
        answer.extend([0]*n)
    else:
        if x < 0:
            end_num = n*x-1
        else:
            end_num = n*x+1
        for i in range(x,end_num,x):
            answer.append(i)
    return answer
