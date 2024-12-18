import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

# 사과가 1개 있는 격자(1), 장애물이 있는 격자(-1), 빈칸으로 되어 있는 격자(0)
# 상, 하, 좌, 우 방향으로 한 칸 이동
# 학생이 지나간 칸은 떠나는 즉시 장애물 칸으로 변경!
# (r,c)에서 세 번 이하의 이동으로 사과를 2개 이상 먹을 수 있으면 1, 아니면 0 출력
# 현재 (r,c)는 빈칸

N = 5
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c = map(int, sys.stdin.readline().split())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(i, j):
    q = deque([(i, j, 0, 0, set({(i, j)}))])

    while q:
        i, j, apples, move, visited = q.popleft()

        if (move > 3): continue
        if (apples >= 2): return 1

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if (0 <= ni < N and  0<= nj < N and arr[ni][nj] != -1 and (ni, nj) not in visited):
                q.append([ni, nj, apples + arr[ni][nj], move + 1, visited.union({(ni, nj)})])
    return 0

def dfs(i, j, apples, move):
    if move > 3: 
        return 0
    if apples >= 2:
        return 1
    
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if (0 <= ni < N and 0 <= nj < N and arr[ni][nj] != -1):
            origin = arr[ni][nj]
            arr[ni][nj] = -1
            if dfs(ni, nj, apples + origin, move + 1):
                return 1
            arr[ni][nj] = origin
    return 0

# print(bfs(r, c))

arr[r][c] = -1
print(dfs(r, c, 0, 0))