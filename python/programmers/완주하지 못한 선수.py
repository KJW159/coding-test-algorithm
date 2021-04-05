from collections import defaultdict


def solution(participant, completion):
    answer = ''
    people_dict = defaultdict(int)
    for people in participant:
        people_dict[people] += 1
    for comp in completion:
        people_dict[comp] -= 1
    for key, val in people_dict.items():
        if val != 0:
            answer = key

    return answer