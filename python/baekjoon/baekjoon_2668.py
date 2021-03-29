# baekjoon_2668 숫자고르기

# v1
# def combinations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in combinations1(arr[i+1:], r-1):
#                 yield [arr[i]] + next
#
#
# N = int(input())
#
# nums = [0]
# for _ in range(N):
#     nums.append(int(input()))
# res = 0
# res_nums = None
#
# for pick in range(1, N+1):
#     for comb in combinations1(range(1,N+1), pick):
#         pick_nums = set()
#         for idx in comb:
#             pick_nums.add(nums[idx])
#         pick_idx = set(comb)
#         if pick_idx == pick_nums:
#             res = max(res, len(pick_nums))
#             res_nums = pick_nums
# print(res)
# res_nums = sorted(res_nums)
# for num in res_nums:
#     print(num)

# v2

def dfs(idx, visited):
    visited_tmp = visited[:]
    stack = []
    stack.append(idx)
    visited_tmp[idx] = 1
    trg_tmp = False
    ans_tmp = []

    while stack:
        idx_tmp = stack.pop()
        num_tmp = nums[idx_tmp]
        if visited_tmp[num_tmp] == 1 and num_tmp == idx:
            ans_tmp.append(num_tmp)
            trg_tmp = True
            break
        if visited_tmp[num_tmp] == 0:
            stack.append(num_tmp)
            visited_tmp[num_tmp] = 1
            ans_tmp.append(num_tmp)
    return trg_tmp, ans_tmp

N = int(input())

nums = [0]
for _ in range(N):
    nums.append(int(input()))

visited = [0]*(N+1)
res = set()
for idx in range(1, N+1):
    trg, ans = dfs(idx, visited)
    if trg:
        for i in ans:
            if visited[i] == 0:
                visited[i] = 1
                res.add(i)
print(len(res))
res = sorted(res)
for j in res:
    print(j)