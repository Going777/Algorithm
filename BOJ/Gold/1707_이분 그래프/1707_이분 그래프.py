import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline())

def dfs(v, adjLst, visited, flag):
    visited[v] = flag

    for t in adjLst[v]:
        if visited[t] == flag: # 인접한 노드가 같은 집합이라면 이분 그래프 아님
            return False
        if visited[t] == -1: # 방문하지 않은 노드에 대해서 재귀 탐색
            if not dfs(t, adjLst, visited, 1 - flag): # 반대 색으로 탐색한 결과가 이분 그래프가 아니라는 결과라면
                return False # False 반환
    
    return True

def bfs(v, adjLst, visited):
    visited[v] = 0
    q = deque([v])

    while q:
        i = q.popleft()

        for t in adjLst[i]:
            if (visited[t] == visited[i]):
                return False
            if visited[t] == -1:
                q.append(t)
                visited[t] = 1 - visited[i]
    
    return True

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    adjLst = [[] for _ in range(V+1)]
    visited = [-1] * (V + 1) # -1: 미방문, 0: 집합1, 1: 집합2
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        adjLst[a].append(b)
        adjLst[b].append(a)

    is_binary = True
    for v in range(1, V + 1):
        if visited[v] == -1: # 방문하지 않은 경우 탐색
            if (not bfs(v, adjLst, visited)): # bfs 탐색
            # if (not dfs(v, adjLst, visited, 0)): # dfs 탐색
                is_binary = False
                break

    print("YES" if is_binary else "NO")