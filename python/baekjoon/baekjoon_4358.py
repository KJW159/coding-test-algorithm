# baekjoon_4358 생태학

# v1
import sys
from collections import defaultdict


trees = defaultdict(int)
total_num = 0
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    trees[tree] += 1
    total_num += 1

trees = sorted(trees.items())
for key, val in trees:
    print("{} {:.4f}".format(key, (val/total_num)*100))