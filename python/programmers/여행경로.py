from collections import defaultdict, OrderedDict

# v1
# def solution(tickets):
#     answer = []
#
#     def dfs(start):
#         stack = [start]
#         answer.append(start)
#
#         while stack:
#             start = stack.pop()
#             if start in tickets_dict.keys():
#                 tickets_dict[start].sort()
#                 for end in tickets_dict[start]:
#                     if end not in answer:
#                         stack.append(end)
#                         answer.append(end)
#
#     tickets_dict = defaultdict(list)
#     for i in range(len(tickets)):
#         tickets_dict[tickets[i][0]].append(tickets[i][1])
#     for start in tickets_dict.keys():
#         if start not in answer:
#             dfs(start)
#
#     return answer

# v2
# def solution(tickets):
#     answer = []
#
#     def dfs(start):
#         stack = [start]
#         answer.append(start)
#
#         while stack:
#             s1 = stack.pop()
#             for e1 in tickets_dict[s1]:
#                 if e1 not in answer:
#                     stack.append(e1)
#                     answer.append(e1)
#
#     tickets_dict = defaultdict(list)
#     for i in range(len(tickets)):
#         tickets_dict[tickets[i][0]].append(tickets[i][1])
#     for key in tickets_dict.keys():
#         tickets_dict[key].sort()
#     print(tickets_dict)
#     dfs("ICN")
#
#     return answer

from collections import defaultdict
def solution(tickets):
    answer = []

    def dfs(start):
        stack = [start]

        while stack:
            start = stack[-1]
            if not tickets_dict[start]:
                answer.append(stack.pop())
            else:
                stack.append(tickets_dict[start].pop())


    tickets_dict = defaultdict(list)
    for i in range(len(tickets)):
        tickets_dict[tickets[i][0]].append(tickets[i][1])
    for key in tickets_dict.keys():
        tickets_dict[key].sort(reverse=True)
    dfs("ICN")
    answer.reverse()

    return answer


n = int(input())
tickets = [list(input().split(',')) for _ in range(n)]
print(solution(tickets))