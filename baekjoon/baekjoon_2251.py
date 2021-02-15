# baekjoon_2251 물통

# import collections
#
# def bfs():
#     queue = collections.deque()
#     queue.append([0, 0, bottle[2]])
#     visited = collections.defaultdict(list)
#     visited[0].append([0, bottle[2]])
#     bottle_c = []
#
#     while queue:
#         water = queue.popleft()
#
#         if water[0] == 0:
#             bottle_c.append(water[2])
#         # ways s(from), e(to)
#         for s, e in ways:
#             water_tmp = water[:]
#             if water[s]+water[e] > bottle[e]:
#                 water_tmp[s] = water[s]+water[e]-bottle[e]
#                 water_tmp[e] = bottle[e]
#             else:
#                 water_tmp[s] = 0
#                 water_tmp[e] = water[s]+water[e]
#             if water_tmp[1:] not in visited[water_tmp[0]]:
#                 queue.append(water_tmp)
#                 visited[water_tmp[0]].append([water_tmp[1], water_tmp[2]])
#
#     return bottle_c
#
# def permutations1(arr, r):
#     for i in range(len(arr)):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for next in permutations1(arr[:i]+arr[i+1:], r-1):
#                 yield [arr[i]]+next
#
#
# bottle = list(map(int, input().split()))
#
# ways = []
# for w in permutations1([0,1,2], 2):
#     ways.append(w)
#
# res = bfs()
# res.sort()
# for i in res:
#     print(i, end=" ")


# re-v1

from collections import deque


def permutations1(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations1(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next

def bfs(bottle_max):
    queue = deque()
    queue.append([0,0,bottle_max[2]])
    visited.append([0,0,bottle_max[2]])

    while queue:
        curr = queue.popleft()
        if curr[0] == 0:
            water.add(curr[2])
        for b1, b2 in permutations1([0,1,2], 2):
            curr_tmp = curr[:]
            tmp = curr[b1] + curr[b2]
            if tmp > bottle_max[b1]:
                curr_tmp[b2] = tmp-bottle_max[b1]
                curr_tmp[b1] = bottle_max[b1]
            else:
                curr_tmp[b2] = 0
                curr_tmp[b1] = tmp
            if curr_tmp not in visited:
                queue.append(curr_tmp)
                visited.append(curr_tmp)


bottle_max = list(map(int, input().split()))
water = set()
visited = []
bfs(bottle_max)
water = sorted(water)
print(*water)
