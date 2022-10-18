from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = di + i, dj + j
            if 0 <= ni < N and 0<= nj < N and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                q.append([ni,nj])
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

tot = 0
cnts = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            tot += 1
            arr[i][j] = 0
            cnts.append(bfs(i, j))

print(tot)
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