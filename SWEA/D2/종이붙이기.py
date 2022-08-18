def calc(N):
    lst = [0] * (N+1)
    lst[1], lst[2] = 1, 3
    for i in range(3, N + 1):
        lst[i] = lst[i-1] + lst[i-2]*2
    return lst

T = int(input())
for t in range(1, 1+T):
    N = int(input()) // 10
    max_N = 300
    memo = calc(max_N)
    print(f"#{t} {memo[N]}")