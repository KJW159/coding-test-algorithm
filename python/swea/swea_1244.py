# swea_1244 최대 상금

# v1
# def dfs(idx, cnt, num):
#     global res
#     # cnt가 max_cnt일 때
#     if cnt == max_cnt:
#         if num > res:
#             res = num
#         return
#     num_tmp = list(str(num))
#     for i in range(idx+1, len(num_tmp)):
#         num_tmp2 = num_tmp[:]
#         num_tmp2[i], num_tmp2[idx] = num_tmp2[idx], num_tmp2[i]
#         if num_tmp2[0] != 0:
#             num_int = int(''.join(num_tmp2))
#             if visited[num_int] == 0:
#                 visited[num_int] = 1
#                 dfs(idx+1, cnt+1, num_int)
#
#
# T = int(input())
#
# for t in range(1, T+1):
#     num, max_cnt = map(int, input().split())
#     res = 0
#     visited = [0]*1000000
#     visited[num] = 1
#     dfs(0, 0, num)
#     print("#{} {}".format(t, res))


# v2
# def dfs(idx, cnt, nums, num_int):
#     global res
#     # cnt가 max_cnt일 때
#     if num_int > res:
#         res = num_int
#     if cnt == max_cnt:
#         return
#     for i in range(idx+1, len(nums)):
#         num_tmp = nums[:]
#         num_tmp[i], num_tmp[idx] = num_tmp[idx], num_tmp[i]
#         if num_tmp[0] != 0:
#             num_int = int(''.join(num_tmp))
#             if visited[num_int] == 0:
#                 visited[num_int] = 1
#                 dfs(idx+1, cnt+1, nums, num_int)
#
#
# T = int(input())
#
# for t in range(1, T+1):
#     num, max_cnt = map(int, input().split())
#     res = num
#     visited = [0]*1000000
#     visited[num] = 1
#     dfs(0, 0, list(str(num)), num)
#     print("#{} {}".format(t, res))



# v3
# def dfs(cnt, num_int):
#     global res
#     if num_int > res:
#         res = num_int
#     # cnt가 max_cnt일 때
#     if cnt == max_cnt:
#         return
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             nums[i], nums[j] = nums[j], nums[i]
#             if nums[0] != 0:
#                 num_int = int(''.join(nums))
#                 if visited[num_int] == 0:
#                     visited[num_int] = 1
#                     dfs(cnt+1, num_int)
#             nums[i], nums[j] = nums[j], nums[i]
#
#
# T = int(input())
#
# for t in range(1, T+1):
#     num, max_cnt = map(int, input().split())
#     res = num
#     visited = [0]*1000000
#     visited[num] = 1
#     nums = list(str(num))
#     dfs(0, num)
#     print("#{} {}".format(t, res))


# v4
# def dfs(cnt, num_int):
#     global res
#     # cnt가 max_cnt일 때
#     if cnt == max_cnt:
#         print(num_int, cnt)
#         # visited[num_int] = 1
#         if num_int > res:
#             res = num_int
#         return
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             nums[i], nums[j] = nums[j], nums[i]
#             if nums[0] != 0:
#                 num_int = int(''.join(nums))
#                 if visited[num_int] == 0:
#                     print(num_int, cnt)
#                     dfs(cnt+1, num_int)
#             nums[i], nums[j] = nums[j], nums[i]
#
#
# T = int(input())
#
# for t in range(1, T+1):
#     num, max_cnt = map(int, input().split())
#     res = -1
#     res2=0
#     visited = [0]*1000000
#     visited[num] = 1
#     nums = list(str(num))
#     dfs(0, num)
#     print("#{} {}".format(t, res))


# v5
from collections import defaultdict


def dfs(cnt, num_int):
    global res
    # cnt가 max_cnt일 때
    if cnt == max_cnt:
        if num_int > res:
            res = num_int
        return
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            if nums[0] != 0:
                num_int = int(''.join(nums))
                if visited[(num_int, cnt+1)] == 0:
                    visited[(num_int, cnt+1)] = 1
                    dfs(cnt+1, num_int)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())

for t in range(1, T+1):
    num, max_cnt = map(int, input().split())
    res = -1
    visited = defaultdict(int)
    visited[(num,0)] = 1
    nums = list(str(num))
    dfs(0, num)
    print("#{} {}".format(t, res))