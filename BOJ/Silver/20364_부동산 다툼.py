import sys
input = sys.stdin.readline

def solve(n):
    c = n
    p = c // 2
    ans = 0
    while p >= 1:
        if check[p]:
            ans = tree[p]
        c = p
        p = c // 2
    return ans

N, Q = map(int, input().split())    # N: 땅 개수 / Q: 오리 수
tree = [0] + list(range(1, N+1))
check = [0] * (N+1)
for _ in range(Q):
    n = int(input())
    check[n] = 1
    print(solve(n))

'''
6 4
5
6
2
4
'''
'''
13 6
3
5
6
2
12
13
'''