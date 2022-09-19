import sys
input = sys.stdin.readline

def dfs(n):
    global cnt
    visited[n] = 1
    for t in adjLst[n]:
        if not visited[t]:
            dfs(t)
            cnt += 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())    # N: 국가 수 / M: 비행기 종류
    adjLst = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)

    cnt = 0
    visited = [0]*(N+1)
    dfs(1)
    print(cnt)

'''
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5
'''
'''
1
5 4
2 1
1 3
4 2
2 5
'''