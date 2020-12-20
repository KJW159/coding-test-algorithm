# baekjoon_1021
import collections

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))

que = collections.deque(range(1,N+1))

cnt = 0
for num in nums:
    if que.index(num) <= len(que)//2:
        while True:
            num_w = que.popleft()
            if num != num_w:
                que.append(num_w)
                cnt += 1

            else:
                break
    else:
        while True:
            if num != que[0]:
                que.appendleft(que.pop())
                cnt += 1
            else:
                que.popleft()
                break

print(f'{cnt}')


