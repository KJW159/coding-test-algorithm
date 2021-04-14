# baekjoon_1759 암호 만들기

# v1
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield arr[i]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield arr[i] + next
#
# L, C = map(int, input().split())
# chars = list(input().split())
#
# chars1 = []
# chars2 = []
# vowel = ['a','e','o','i','u']
# # chars 1 - 모음 , chars 2 - 자음.
# for char in chars:
#     if char in vowel:
#         chars1.append(char)
#     else:
#         chars2.append(char)
# res = []
# for c1 in range(1, L-1):
#     tmp = []
#     tmp.extend(combinations1(chars1, c1))
#     # for _ in range()
#     tmp.extend(combinations1(chars2, L-c1))
#     tmp.sort()
#     print(tmp)
#     # res_tmp = "".join(tmp)
#     # if res_tmp not in res:
#     #     res.append(res_tmp)
#     tmp = []
# # print(res)


# v2
def combinations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations1(arr[i+1:], r-1):
                yield [arr[i]] + next

L, C = map(int, input().split())
chars = list(input().split())

vowel = ['a','e','o','i','u']
chars.sort()
comb_pwd = combinations1(chars, L)
for pwd in comb_pwd:
    cnt = 0
    for char in pwd:
        if char in vowel:
            cnt += 1
    if cnt >=1 and L-cnt >= 2:
        print("".join(pwd))