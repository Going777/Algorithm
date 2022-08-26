from itertools import combinations
def multiply(lst):
    n = 1
    for c in lst:
        n *= c
    return n

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())    # N: 달란트 수 / P: 묶음 수

    Q = N // P
    R = N % P
    ans = 1
    for _ in range(P-R):
        ans *= Q
    for _ in range(R):
        ans *= (Q+1)

    print(f"#{tc} {ans}")

'''
10
10 3
20 5
30 9
40 12
50 12
60 23
70 23
80 32
90 32
100 32
'''