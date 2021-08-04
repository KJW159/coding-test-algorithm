# baekjoon_1929 소수 구하기

# v1
from math import sqrt


M, N = map(int, input().split())
arr = [True for _ in range(N+1)]

for i in range(2, int(sqrt(N))+1):
    if arr[i]:
        j = 2
        while i*j <= N:
            if arr[i*j]:
                arr[i*j] = False
            j += 1

for num in range(M,N+1):
    if num == 1:
        continue
    if arr[num]:
        print(num)