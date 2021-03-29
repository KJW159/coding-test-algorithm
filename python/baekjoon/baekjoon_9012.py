# baekjoon_9012 괄호

N = int(input())

ps = [input() for n in range(N)]


for strings in ps:
    res = None
    stack = []
    trg = 0
    for string in strings:
        if string == '(':
            stack.append(string)

        if string == ')' and stack:
            stack.pop()
        elif string == ')' and not stack:
            trg = 1
            break
    if stack or trg == 1:
        res = 'NO'
    elif not stack:
        res = 'YES'
    print(f'{res}')
