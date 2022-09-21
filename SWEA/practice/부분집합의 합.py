# def f(n, r, s, sm):
#     global ans
#     if sm > K:
#         return
#     if r == 0:
#         if sm == K:
#             ans += 1
#         return
#     for i in range(s, n-r+1):
#         f(n, r-1, i+1, sm+lst[i])
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())  # N: 부분집합 개수 / K: 합 타겟값
#     lst = list(range(1, 13))            # 1~12까지의 원소
#     ans = 0
#     f(12, N, 0, 0)
#     print(f'#{tc} {ans}')

# -------------------------------------------------------------------------

def dfs(n, sm, cnt):    # n: 배열의 인덱스
    global ans
    # 가지치기
    if sm > K:
        return
    # 종료조건(n에 관련)
    if n == N:
        # 정답처리
        if sm == K and cnt == M:
            ans += 1
        return
    # 하부함수 호출
    dfs(n+1, sm+lst[n], cnt+1)  # n번 인덱스를 사용하는 경우
    dfs(n+1, sm, cnt)           # n번 인덱스를 사용하지 않는 경우

T = int(input())
for tc in range(1, T+1):
    M, K = map(int, input().split())    # M: 부분집합 개수 / K: 합 타겟값
    lst = list(range(1, 13))            # 1~12까지의 원소
    N = len(lst)                        # 리스트 길이(12)
    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')

'''
3
3 6
5 15
5 10
'''