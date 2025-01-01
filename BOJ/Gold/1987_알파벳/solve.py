import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우 이동가능
# 새로 이동한 칸에 적힌 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 달라야 한다

def bfs(i, j):
    global ans
    q = set()
    q.add((i, j, arr[i][j]))
    
    while q:
        i, j, alphas = q.pop()
        print(alphas)
        ans = max(ans, len(alphas))

        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] not in alphas:
                q.add((ni, nj, alphas + arr[ni][nj]))

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
ans = 0
bfs(0,0)
print(ans)