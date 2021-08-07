# baekjoon_2960 에라토스테네스의 체

# v1
def finding_num():
    global cnt
    for i in range(2, N+1):
        if arr[i] == 1:
            arr[i] = 0
            cnt += 1
            if cnt == K:
                return i
            j = 2
            while i * j < N+1:
                if arr[i*j]:
                    arr[i*j] = 0
                    cnt += 1
                if cnt == K:
                    return i*j
                j += 1

N, K = map(int, input().split())

arr = [1]*(N+1)
cnt = 0
res = finding_num()
print(res)