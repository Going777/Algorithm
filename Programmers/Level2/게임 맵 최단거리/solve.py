from collections import deque

def solution(maps):
    answer = -1
    N, M = len(maps), len(maps[0])

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = deque([(0, 0)])

    while q:
        i, j = q.popleft()
        if (i == N -1 and j == M - 1):
            answer = visited[i][j]
            break

        for di, dj in ([0,1],[0,-1],[1,0],[-1,0]):
            ni, nj = i + di, j + dj

            if (0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and not visited[ni][nj]):
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))