import sys
input = sys.stdin.readline

def dfs(n, sm):
    global ans

    if ans < sm:
        return
    
    if n == N:
        if sm >= B:
            ans = min(ans, sm)
        return
    
    dfs(n+1, sm + lst[n])
    dfs(n+1, sm)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 10000 * N

    dfs(0, 0)

    print(f"#{t} {ans-B}")