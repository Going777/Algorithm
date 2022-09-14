from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, t):
    q = deque()

    q.append([i, j])
    arr[i][j] = "C"
    cnt = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == t:
                q.append([ni, nj])
                arr[ni][nj] = "C"
                cnt += 1
    return cnt**2

M, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

w_power = b_power = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "W":
            w_power += bfs(i, j, "W")
        elif arr[i][j] == "B":
            b_power += bfs(i, j, "B")
print(w_power, b_power)

'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
'''