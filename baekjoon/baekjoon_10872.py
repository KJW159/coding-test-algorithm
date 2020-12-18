# baekjoon_10872 팩토리얼

def fac(num):
    if 0 <= num <= 12:
        if num == 0 or num == 1:
            return 1
        else:
            return num * fac(num-1)


N = int(input())
result = fac(N)
print(f'{result}')