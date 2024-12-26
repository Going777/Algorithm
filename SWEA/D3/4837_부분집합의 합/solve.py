import sys
input = sys.stdin.readline

def dfs(n, sm, cnt):
    global ans
    # 가지치기
    if sm > K:
        return

    # 종료조건
    if n == N:
        if sm == K and cnt == N:
            ans += 1
        return
    
    # 사용하는 경우
    dfs(n+1, sm + lst[n], cnt+1)
    # 사용하지 않는 경우
    dfs(n+1, sm, cnt)
    
T = int(input())
for t in range(1, T+1):
  N, K = map(int, input().split())
  lst = [n for n in range(1, 13)]
  ans = 0
  dfs(0,0,0)

  print(f"#{t} {ans}")