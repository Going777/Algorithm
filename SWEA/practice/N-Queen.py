'''
NxN의 체스보드에 N개 퀸을 서로 공격하지 못하게 놓고자 한다
    퀸은 같은 행, 열, 대각선 위에 있는 말을 공격할 수 있다
서로 공격할 수 없게 놓을 수 있는 경우의 수는?
'''

# 체크 함수를 만들어 직접 다 체크해보는 형식 >> 시간 오래 걸림
# def check(si, sj):
#     # 위쪽 방향 체크
#     for i in range(si):
#         if arr[i][sj]:
#             return False
#     # 좌상향 대각선 방향 체크
#     i = si - 1; j = sj - 1
#     while i>=0 and j>=0:
#         if arr[i][j]:
#             return False
#         i -= 1 ; j -= 1
#     # 우상향 대각선 방향 체크
#     i = si - 1; j = sj + 1
#     while i>=0 and j<N:
#         if arr[i][j]:
#             return False
#         i -= 1 ; j += 1
#     return True
#
# def dfs(n):
#     global ans
#     if n == N:
#         ans += 1
#         return
#     for j in range(N):
#         if check(n, j):
#             arr[n][j] = 1
#             dfs(n+1)
#             arr[n][j] = 0

# ------------------------------------------------------------------------

# lookup tabel 형식
def dfs2(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if j not in v1 and (n+j) not in v2 and (n-j) not in v3:
            v1.append(j) ; v2.append(n+j); v3.append(n-j)
            dfs2(n+1)
            v1.pop(); v2.pop(); v3.pop()

# ------------------------------------------------------------------------

def solve(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        visited[n] = j      # [n,j]열에 퀸을 배치하겠다는 의미
        for i in range(n):  # 놓을 수 있는 지점인지 검사(현재 놓은 행 이전까지만)
            if (visited[n] == visited[i]) or (n-i == abs(visited[n]-visited[i])):   # 열 검사 & 대각선 검사
                break
        else:               # 놓을 수 있는 경우, 다음 단계로 넘어감
            solve(n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0]*N
    arr = [[0]*N for _ in range(N)]
    ans = 0
    v1,v2,v3=[],[],[]
    # dfs(n)
    dfs2(0)
    solve(0)
    print(f'#{tc} {ans}')

'''
2
1
2
'''