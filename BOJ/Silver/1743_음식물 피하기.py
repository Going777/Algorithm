from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()

    q.append([i, j])
    arr[i][j] = 2
    s = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                q.append([ni, nj])
                arr[ni][nj] = 2
                s += 1
    return s

N, M, K = map(int, input().split()) # K: 음식물 쓰레기 개수
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

mx = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            mx = max(mx, bfs(i, j))
print(mx)
'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''