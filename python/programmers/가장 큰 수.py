
# v1
from itertools import permutations


def solution(numbers):
    answer = 0
    for nums in permutations(numbers):
        num_tmp = ''
        if nums[0] == 0:
            continue
        for num in nums:
            num_tmp += str(num)
        answer = max(answer, int(num_tmp))

    answer = str(answer)
    return answer


# v2