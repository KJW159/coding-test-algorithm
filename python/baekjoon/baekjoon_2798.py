# baekjoon_2798 블랙잭

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next


N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
gap = M
result = 0
for card in combinations(cards, 3):
    sum_c = sum(card)
    gap_tmp = abs(M-sum_c)
    if sum_c <= M and gap_tmp < gap:
        gap = gap_tmp
        result = sum_c
print(f'{result}')


