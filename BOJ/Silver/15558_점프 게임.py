from collections import deque
import sys
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    visisted = [[0]*N for _ in range(2)]

    q.append([i, j, 0])
    visisted[i][j] = 1

    while q:
        i, j, cnt = q.popleft()
        for ni, nj in [(i, j-1), (i, j+1), (int(not i), j+K)]:
            if nj >= N:
                return 1
            if cnt < nj and not visisted[ni][nj] and arr[ni][nj] == 1:
                q.append([ni, nj, cnt+1])
                visisted[ni][nj] = 1
    return 0

N, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(2)]
# 0이면 갈 수 없고, 1이면 갈 수 있다
# 한 칸 앞/뒤로 이동 가능 (i+1 / i-1)
# 반대편 줄 k칸 앞으로 이동 가능 (i+k)
dj = [-1, 1, K]

ans = bfs(0,0)
print(ans)