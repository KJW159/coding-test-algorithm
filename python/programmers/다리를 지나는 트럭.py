from collections import deque

# v1
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     on_bridge = deque()
#     passed = deque()
#     cnt = 0
#     i = 0
#     truck_num = len(truck_weights)
#     while True:
#         if truck_weights[i] <= weight:
#             on_bridge.append(truck_weights[i])
#         cnt += 1
#         if i < truck_num-1:
#             i += 1
#         if cnt % bridge_length == 1 and cnt >= bridge_length:
#             passed.append(on_bridge.popleft())
#         if len(passed) == truck_num:
#             answer = cnt
#             break
#
#     return answer

# v2
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     truck = deque(truck_weights)
#     on_bridge = deque()
#     passed = deque()
#     cnt = 0
#     truck_num = len(truck_weights)
#     while True:
#         if len(passed) == truck_num:
#             answer = cnt
#             break
#         if len(truck) != 0:
#             truck_weight = truck.popleft()
#             if truck_weight <= weight:
#                 on_bridge.append(truck_weight)
#         cnt += 1
#
#         if cnt >= bridge_length and cnt % bridge_length == 0:
#             passed.append(on_bridge.popleft())
#
#     return answer
#
# a,b= map(int, input().split())
# c = list(map(int, input().split()))
# print(solution(a,b,c))


# v3
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     truck = deque(truck_weights)
#     on_bridge = deque()
#     passed_num = 0
#     cnt = 0
#     truck_num = len(truck_weights)
#     while True:
#         cnt += 1
#         if passed_num == truck_num:
#             answer = cnt
#             break
#         if len(truck) != 0:
#             if (sum(on_bridge) + truck[0]) <= weight:
#                 on_bridge.append(truck.popleft())
#             else:
#                 on_bridge.append(0)
#         if cnt >= bridge_length and len(on_bridge) != 0:
#             if on_bridge.popleft() !=0:
#                 passed_num += 1
#     return answer



# v4
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     truck = deque(truck_weights)
#     on_bridge = deque()
#     passed_num = 0
#     cnt = 0
#     truck_num = len(truck_weights)
#     while True:
#         cnt += 1
#         if passed_num == truck_num:
#             answer = cnt
#             break
#         if truck:
#             if (sum(on_bridge) + truck[0]) <= weight:
#                 on_bridge.append(truck.popleft())
#             else:
#                 on_bridge.append(0)
#         if cnt >= bridge_length and on_bridge:
#             if on_bridge.popleft() !=0:
#                 passed_num += 1
#     return answer



# v5
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     truck = deque(truck_weights)
#     on_bridge = deque([0]*bridge_length)
#     cnt = 0
#     while True:
#         if not on_bridge:
#             answer = cnt
#             break
#         cnt += 1
#         on_bridge.popleft()
#         if truck:
#             if (sum(on_bridge) + truck[0]) <= weight:
#                 on_bridge.append(truck.popleft())
#             else:
#                 on_bridge.append(0)
#     return answer

# v6
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     # truck = deque(truck_weights)
#     on_bridge = deque([0]*bridge_length)
#     cnt = 0
#     while True:
#         if not on_bridge:
#             answer = cnt
#             break
#         cnt += 1
#         on_bridge.popleft()
#         if truck_weights:
#             if (sum(on_bridge) + truck_weights[0]) <= weight:
#                 on_bridge.append(truck_weights.pop(0))
#             else:
#                 on_bridge.append(0)
#     return answer

#v7
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     # truck = deque(truck_weights)
#     on_bridge = deque([0]*bridge_length)
#     cnt = 0
#     while on_bridge:
#         cnt += 1
#         on_bridge.popleft()
#         if truck_weights:
#             if (sum(on_bridge) + truck_weights[0]) <= weight:
#                 on_bridge.append(truck_weights.pop(0))
#             else:
#                 on_bridge.append(0)
#     answer = cnt
#     return answer

# v8
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     truck = deque(truck_weights)
#     on_bridge = deque([0]*bridge_length)
#     cnt = 0
#     while on_bridge:
#         cnt += 1
#         on_bridge.popleft()
#         if truck:
#             if (sum(on_bridge) + truck[0]) <= weight:
#                 on_bridge.append(truck.popleft())
#             else:
#                 on_bridge.append(0)
#     answer = cnt
#     return answer


# v9
from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    on_bridge = [0]*bridge_length
    cnt = 0
    while on_bridge:
        cnt += 1
        on_bridge.pop(0)
        if truck:
            if (sum(on_bridge) + truck[0]) <= weight:
                on_bridge.append(truck.popleft())
            else:
                on_bridge.append(0)
    answer = cnt
    return answer

a,b= map(int, input().split())
c = list(map(int, input().split()))
print(solution(a,b,c))