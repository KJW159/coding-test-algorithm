# baekjoon_1966

import collections

T = int(input())

for tc in range(T):
    N, P = list(map(int, input().split()))
    que = collections.deque(map(int, input().split()))
    cnt = 0
    while que:
        max_n = max(que)
        num = que.popleft()
        if num < max_n:
            que.append(num)
            if P <= 0:
                P = len(que)-1
            else:
                P -= 1
        else:
            cnt += 1
            if P == 0:
                break
            else:
                P -= 1
    print(f'{cnt}')


