# def solve(n, cnt):
#     global mn_cnt
#     if cnt >= mn_cnt:
#         return
#     if n == N-1:
#         if cnt < mn_cnt:
#             mn_cnt = cnt
#         return
#     for i in range(1, lst[n]+1):
#         solve(n+i, cnt+1)

def solve(n, cnt, sm):
    global mn_cnt
    if mn_cnt <= cnt:
        return
    if n == N:
        mn_cnt = cnt
        return
    # 배터리 교체하지 않는 경우
    if sm > 0:  # 배터리 잔량이 0이상일때 배터리 교체안할 수 있음
        solve(n+1, cnt, sm - 1)
    # 배터리 교체하는 경우
    solve(n+1, cnt+1, lst[n]-1)

T = int(input())
for tc in range(1, T+1):
    N, *lst = list(map(int, input().split()))
    mn_cnt = N
    solve(0, -1)
    print(f'#{tc} {mn_cnt}')

'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''