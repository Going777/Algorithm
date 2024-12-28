import sys
input = sys.stdin.readline

T = int(input())

def dfs(i, j, cnt, numStr):
    global ans
    if (cnt == 7):
        ans.add(int(numStr))
        return

    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i + di, j + dj
        if (0 <= ni < N and 0 <= nj < N):
            dfs(ni, nj, cnt + 1, numStr + str(arr[ni][nj]))

for t in range(1, T+1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = set()

    for i in range(N):
        for j in range(N):
            dfs(i, j, 1, str(arr[i][j]))
    
    print(f"#{t} {len(ans)}")