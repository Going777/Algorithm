import sys
input = sys.stdin.readline

def solve(n):
    c = n
    ans = 0
    while c:
        if check[c]:
            ans = tree[c]
        c //= 2
    check[n] = 1
    return ans

N, Q = map(int, input().split())    # N: 땅 개수 / Q: 오리 수
tree = [0] + list(range(1, N+1))
check = [0] * (N+1)
for _ in range(Q):
    n = int(input())
    print(solve(n))

'''
6 4
6
6
6
6
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