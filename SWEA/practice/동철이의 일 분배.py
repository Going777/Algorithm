'''
회사에는 N명의 직원이 있다
해야할 일 N개가 생겼다
직원들의 번호가 1부터 N까지 매겨져 있고, 해야할 일도 1부터 N까지 번호가 매겨져 있을 때,
    행렬에 나타나는 값은 i번 직원이 j번 일을 하면 성공할 확률을 나타낸다
직원들에게 할 일을 하나씩 배분할 때, 주어진 일이 모두 성공할 확률의 최댓값은?
'''
def solve(n, p):
    global mx_p
    if p <= mx_p:
        return
    if n==N:
        if p > mx_p:
            mx_p = p
        return
    for j in range(N):
        if not visited[j]:
            if mx_p and arr[n][j] == 0:
                continue
            visited[j] = 1
            solve(n+1, p*arr[n][j]*0.01)
            visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    mx_p = 0
    solve(0,1)
    print(f'#{tc} {format(mx_p*100, ".6f")}')

'''
1
3
13 0 50
12 70 90
25 60 100
'''