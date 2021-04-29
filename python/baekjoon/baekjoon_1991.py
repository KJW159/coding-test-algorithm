# baekjoon_1991 트리 순회


from collections import defaultdict

# 전위 순회
def preorder(root):
    global res
    res += root

    for node in nodes[root]:
        if node != '.':
            preorder(node)
    return


def inorder(root):
    global res
    if nodes[root][0] == '.' and nodes[root][1] == '.':
        res += root
        return
    for node in nodes[root]:
        if node != '.':
            inorder(node)
        if root not in res:
            res += root

def postorder(root):
    global res
    if nodes[root][0] == '.' and nodes[root][1] == '.':
        res += root
        return
    for node in nodes[root]:
        if node != '.':
            postorder(node)
    # if root not in res:
    res += root

N = int(input())

nodes = defaultdict(list)
for _ in range(N):
    x, y, k = input().split()
    nodes[x] = [y, k]

for i in range(3):
    res = ''
    if i == 0:
        preorder('A')
        print(res)
    elif i == 1:
        inorder('A')
        print(res)
    else:
        postorder('A')
        print(res)

