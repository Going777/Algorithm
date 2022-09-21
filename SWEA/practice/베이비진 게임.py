def solve(n):
    global ans
    if n == N-1:
        cnt = 0
        for i in range(0, N, 3):
            if (lst[i] == lst[i+1] == lst[i+2]) or (lst[i]+2 == lst[i+1]+1 == lst[i+2]):
                cnt += 1
        if cnt == 2:
            ans = 1
        return
    for i in range(n, N):
        lst[n], lst[i] = lst[i], lst[n]
        solve(n+1)
        lst[n], lst[i] = lst[i], lst[n]

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    N = len(lst)
    ans = 0
    solve(0)
    print(f'#{tc} {ans}')

'''
3
444345
102034
667767
'''