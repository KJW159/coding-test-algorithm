# baekjoon_10951 A+B-4

while True:
    result = 0
    try:
        a, b = list(map(int, input().split()))
        result = a + b
        print(result)
    except:
        break