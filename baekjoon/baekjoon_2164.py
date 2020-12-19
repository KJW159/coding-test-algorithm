import collections

N = int(input())

deq = collections.deque()

for n in range(1, N+1):
    deq.append(n)

while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())

res = deq.pop()
print(f'{res}')


