# baekjoon_10870

def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

N = int(input())
result = fibonacci(N)
print(f'{result}')