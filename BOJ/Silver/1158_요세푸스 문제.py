import sys
N, K = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))
result = ["<"]
i = 0
while True:
    if len(result) >= len(arr):
        break
    if i == K-1:
        result.append(arr[i])
    i += 1
    K += K
    if K >= len(arr):
        K = K % len(arr)