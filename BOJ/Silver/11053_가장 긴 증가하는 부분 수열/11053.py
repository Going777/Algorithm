import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lis = [lst[0]]

for i in range(N):
    if (lst[i] > lis[-1]):
        lis.append(lst[i])
    else:
        pos = bisect_left(lis, lst[i])
        lis[pos] = lst[i]

print(len(lis))