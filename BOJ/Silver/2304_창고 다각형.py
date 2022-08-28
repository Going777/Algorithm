N = int(input())    # 기둥 개수
l_margin = []
height = []
for _ in range(N):
    L, H = map(int, input().split())    # L: 각 기둥의 왼쪽 면의 위치 / H: 높이
    l_margin.append(L)
    height.append(H)

arr = [0] * (max(l_margin)+1)
for idx in range(N):
    arr[l_margin[idx]] = height[idx]

mx_idx = arr.index(max(arr))

ans = 0
tmp = 0
for idx in range(mx_idx+1):
    if tmp < arr[idx]:
        tmp = arr[idx]
    ans += tmp

tmp = 0
for idx in range(len(arr)-1, mx_idx, -1):
    if tmp < arr[idx]:
        tmp = arr[idx]
    ans += tmp

print(ans)

'''
7
2 4
9 10
15 8
4 6
5 3
8 10
13 6
'''
