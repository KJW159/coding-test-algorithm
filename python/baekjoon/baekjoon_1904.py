# baekjoon_1904 01타일

def tile(N):
    for n in range(3, N+1):
        arr[n] = (arr[n-2] + arr[n-1]) % 15746
    return arr[N]

N = int(input())
arr = [0]*1000001

arr[1] = 1
arr[2] = 2

result = tile(N)
print(result)