def solve(n, sm):
    global ans
    # 가지치기
    if sm >= ans:
        return
    # 종료 조건
    if n == N:
        if ans > sm:
            ans = sm
        return
    # 하부 함수
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            solve(n+1, sm+arr[n][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N

    ans = 10*N
    solve(0, 0)

    print(f"#{tc} {ans}")

'''
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9   
3 3 8 3 1   
9 2 8 8 6   
1 5 7 8 3   
5 5 4 6 8  
'''