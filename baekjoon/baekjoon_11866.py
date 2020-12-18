# baekjoon_11866 요세푸스 문제 0

import collections

N, K = list(map(int, input().split()))

deq = collections.deque()

for n in range(1, N+1):
    deq.append(n)

deq.remove()