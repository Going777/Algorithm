T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N: 노드 개수 / M: 리프 노드 개수 / L: 타겟 노드 번호
    tree = [0] * (N+1)
    for _ in range(M):
        i, n = map(int, input().split())
        tree[i] = n
    for c in range(N, 1, -1):
        tree[c//2] += tree[c]

    print(f"#{tc} {tree[L]}")

'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962
'''