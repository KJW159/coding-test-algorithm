# baekjoon_1302 베스트 셀러


# v1
from collections import defaultdict
N = int(input())

dict = defaultdict(int)

for i in range(N):
    title = input()
    dict[title] += 1


res = []
max_num = 0
for title, num in dict.items():
    if num > max_num:
        max_num = num
        if res:
            res = [title]
        else:
            res.append(title)
    elif num == max_num:
        res.append(title)
res.sort()
print(res[0])