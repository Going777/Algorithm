from collections import deque
import sys
input = sys.stdin.readline

def bfs(starts):
    q = deque()

    for i, j, c in starts:
        q.append([i, j, c])

    while q:
        i, j, c = q.popleft()
        if arr[i][j] == "D":
            ans = visited[i][j]
            if ans == -1:
                return "KAKTUS"
            return ans
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 'X':  # 범위 내 & 돌 아닌 경우
                if c == "s":                    # 시작점에서 출발한 경로인 경우
                    if visited[i][j] != -2 and visited[ni][nj] == -1:
                        q.append([ni, nj, c])
                        visited[ni][nj] = visited[i][j] + 1
                elif c == "w":                  # 물에서 시작된 경로인 경우
                    if visited[ni][nj] != -2 and arr[ni][nj] != "D":
                        q.append([ni, nj, c])
                        visited[ni][nj] = -2
    return "KAKTUS"

N, M = map(int, input().split())
# 비어있는 곳은 '.' / 물이 차있는 지역은 '*' / 돌은 'X'
# 비버의 굴은 'D' / 고슴도치 현재 위치 'S'
arr = [list(input()) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

s_lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':            # 돌이 있는 곳은 X로 표시
            visited[i][j] = 'X'
        elif arr[i][j] == "*":          # 물이 찬 곳은 -2로 표시
            s_lst.append([i, j, 'w'])
            visited[i][j] = -2
        elif arr[i][j] == "S":          # 처음 시작 점은 0으로 표시 (1곳)
            s_lst.insert(0, [i, j, 's'])
            visited[i][j] = 0

ans = bfs(s_lst)
print(ans)

'''
2 2
SD
**
'''