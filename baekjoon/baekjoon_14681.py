# baekjoon_14681 사분면 고르기

coordinate = []
result = None
for i in range(2):
    coordinate.append(int(input()))
x, y = coordinate

if x > 0 and y > 0:
    result = 1
elif x < 0 and y > 0:
    result = 2
elif x < 0 and y < 0:
    result = 3
else:
    result = 4

print(result)