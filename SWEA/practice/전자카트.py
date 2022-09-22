# def solve(n, i, tmp_visit, sm):
#     global ans
#     if sm > ans:
#         return
#
#     if n == N:
#         if i == 0:
#             ans = min(ans, sm)
#     if p[i]:
#         return
#
#     for j in range(N):
#         if j not in tmp_visit and arr[i][j] != 0:
#             tmp_visit.append(j)
#             p[i] = arr[i][j]
#             solve(n+1, j, tmp_visit, sm+p[i])
#             tmp_visit.pop()
#             p[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [0]*N
#     visited = [[0]*N for _ in range(N)]
#     ans = 100*10
#     solve(0, 0, [], 0)
#     print(f'#{tc} {ans}')

# ---------------------------------------------------------------------

def dfs(n, i, sm):  # n: 방문하고 있는 구역 수 / i: 현재 구역번호(시작지점) / sm: 배터리량
    global ans
    # 가지치기
    if sm >= ans:
        return
    # 종료조건
    if n == N-1:
        ans = min(ans, sm+arr[i][1])    # 여태까지의 배터리량 + 1번으로 돌아가는 필요량
        return
    # 하부함수 호출
    for j in range(2, N+1):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, j, sm+arr[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N+1)
    ans = 100*10
    visited[1] = 1  # 1번 구역에서 시작하므로, 1번은 방문처리
    dfs(0, 1, 0)
    print(f'#{tc} {ans}')

'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''