import sys
input = sys.stdin.readline

n1, n2 = input().split()
target1, target2 = n1[::-1], n2[::-1]

print(target1) if target1 > target2 else print(target2)