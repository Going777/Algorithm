import sys
from collections import deque

di = [1,-1,0,0]
dj = [0,0,-1,1]

def bfs(i, j):
    q = deque()

    tmp = 1
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.pop()
        arr[i][j] = 2
        for k in range(4):
            ni = i + di[k]; nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == 1:
                tmp += 1
                q.append([ni, nj])
                visited[ni][nj] = 1
    return tmp

N = int(sys.stdin.readline())
# 1은 집이 있는 곳, 0은 집이 없는 곳
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnts = []

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnts.append(bfs(i, j))
            cnt += 1

print(cnt)
[print(x) for x in sorted(cnts)]

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''