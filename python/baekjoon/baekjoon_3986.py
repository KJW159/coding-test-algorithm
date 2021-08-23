# baekjoon_3986 좋은 단어

# v1
# T = int(input())
# res = 0
# for _ in range(T):
#     words = list(input())
#     stack = []
#     trg = True
#     for word in words:
#         if word == 'A':
#             stack.append('A')
#         if stack and word == 'B':
#             stack.pop()
#         elif not stack and word == 'B':
#             trg = False
#             break
#     if stack:
#         trg = False
#     if trg:
#         res += 1
# print(res)


# v2

T = int(input())
res = 0
for _ in range(T):
    words = list(input())
    stack = []
    trg = True
    for word in words:
        if not stack:
            stack.append(word)
        elif stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    if stack:
        trg = False
    if trg:
        res += 1

print(res)