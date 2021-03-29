# baekjoon_2753 윤년

year = int(input())
result = None

if year % 4 == 0 and year % 100 != 0:
    result = 1
elif year % 4 == 0 and year % 400 == 0:
    result = 1
else:
    result = 0

print(result)