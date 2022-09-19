import sys
input = sys.stdin.readline

def solve(arr, h):
    mid = (len(arr)//2)         # 중간값에 해당하는 값이 루트값
    tree[h].append(arr[mid])    # root node
    if len(arr) == 1:
        return
    solve(arr[:mid], h+1)       # left node
    solve(arr[mid+1:], h+1)     # right node


N = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(N)]

solve(lst, 0)
for row in tree:
    print(*row)