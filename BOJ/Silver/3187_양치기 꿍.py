import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    v = k = 0

    tmp = arr[i][j]
    if tmp == "v":
        v += 1
    elif tmp == "k":
        k += 1
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for di,dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni = i + di ; nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] != "#":
                tmp = arr[ni][nj]
                if tmp == "v":
                    v += 1
                elif tmp == "k":
                    k += 1
                q.append([ni, nj])
                visited[ni][nj] = 1
    if k > v:
        v = 0
    else:
        k = 0
    return [v, k]

N, M = map(int, input().split())    # N: 행 수 / M: 열 수
# '.'은 빈공간, '#'은 울타리, 'v'는 늑대, 'k'는 양
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
s = w = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != "#" and not visited[i][j]:
            v, k = bfs(i, j)
            s += k ; w += v
print(s, w)
'''
9 12
.###.#####..
#.kk#...#v#.
#..k#.#.#.#.
#..##k#...#.
#.#v#k###.#.
#..#v#....#.
#...v#v####.
.####.#vv.k#
.......####.
'''