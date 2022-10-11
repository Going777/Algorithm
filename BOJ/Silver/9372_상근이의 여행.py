'''
겨울방학을 맞아 N개국을 여행하기로 했다
최대한 적은 종류의 비행기를 타고 국가를 이동하고자 한다(국가 이동 시, 재방문 가능)
상근이가 모든 국가를 여행하기 위해 타야하는 비행기 종류의 최소 개수는?
'''

import sys
input = sys.stdin.readline

# dfs 풀이
def dfs(n):
    global cnt
    visited[n] = 1
    for t in adjLst[n]:
        if not visited[t]:
            dfs(t)
            cnt += 1

# bfs 풀이
from collections import deque
def bfs(n):
    global cnt
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1
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
    # dfs(1)
    bfs(1)
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