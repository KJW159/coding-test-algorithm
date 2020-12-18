# baekjoon_10828 스택


def push(arr, num):
    num = int(num)
    arr.append(num)
    return

def my_pop(arr):
    if not arr:
        return -1
    num_pop = arr.pop()
    return num_pop

def size(arr):
    num_cnt = len(arr)
    return num_cnt

def my_empty(arr):
    if arr:
        return 0
    if not arr:
        return 1
def top(arr):
    if not arr:
        return -1
    else:
        return arr[-1]

N = int(input())

commands = [list(input().split()) for n in range(N)]
arr = []
for command in commands:
    result = None
    if command[0] == 'push':
        push(arr, command[1])
    elif command[0] == 'top':
        result = top(arr)
    elif command[0] == 'size':
        result = size(arr)
    elif command[0] == 'empty':
        result = my_empty(arr)
    elif command[0] == 'pop':
        result = my_pop(arr)
    if result == None:
        pass
    else:
        print(f'{result}')
