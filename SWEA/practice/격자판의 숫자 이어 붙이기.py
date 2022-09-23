'''
4X4 크기의 격자판 존재 (0~9)
임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서, 각 칸에 있는 숫자를 차례로 이어붙이면 7자리 숫자가 됨
만들 수 있는 서로 다른 일곱 자리 수들의 개수는?
'''

# def solve(n, i, j, tmp):
#     tmp += arr[i][j]
#     if n == 7:
#         visited.add(tmp)
#         return
#     for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#         ni = i + di ; nj = j + dj
#         if 0 <= ni < N and 0 <= nj < N:
#             solve(n+1, ni, nj, tmp)

from collections import deque
def bfs(i, j):
    q = deque()
    q.append([i, j, ''])
    while q:
        i, j, n = q.popleft()
        if len(n) == 7:
            visited.add(n)
        elif len(n) > 7:
            break
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                q.append([ni, nj, n+arr[ni][nj]])

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(input().split()) for _ in range(N)]
    visited = set()
    for i in range(N):
        for j in range(N):
            # solve(1, i, j, '')
            bfs(i, j)
    print(f'#{tc} {len(visited)}')
'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''