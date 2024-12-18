import sys
from collections import deque
input = sys.stdin.readline

# (0,0)에서 시작
# 오른쪽, 아래로만 이동 가능
# 가장 오른쪽, 가장 아래 칸에 도달하는 순간 승리
# 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수만큼
# 끝 점에 도달할 수 있으면 "HaruHaru", 없으면 "Hing" 출력

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def dfs(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()
        if (arr[i][j] == -1):
            return True
        
        d = [(arr[i][j], 0), (-arr[i][j], 0), (0, arr[i][j]), (0, -arr[i][j])]
        for (di, dj) in d:
            ni, nj = i + di, j + dj

            if (0 <= ni < N and 0 <= nj < N and not visited[ni][nj]):
                visited[ni][nj] = 1
                q.append([ni, nj])
        
    return False

print("HaruHaru" if dfs(0,0) else "Hing")