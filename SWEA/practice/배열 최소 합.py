def f(n, sm):
    global ans
    # 가지치기
    if sm >= ans:
        return
    # 종료조건
    if n == N:
        if sm < ans:
            ans = sm
        return
    # 하부함수 호출
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            f(n+1, sm+arr[n][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 10*N
    f(0, 0)
    print(f'#{tc} {ans}')

# -------------------------------------------------------------------

# def f(i, k):
#     global minV
#     if i == k:
#         s = 0
#         for l in range(k):
#             s += arr[l][p[l]]
#         if minV > s:
#             minV = s
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [i for i in range(N)]   # p[i]: i행에서 선택한 열 번호
#     minV = N*10

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