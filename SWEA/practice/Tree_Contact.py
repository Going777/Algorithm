from collections import deque
def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    tmp = []

    q.append(s)
    visited[s] = 1
    while q:
        i = q.popleft()
        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = visited[i] + 1

    for idx in range(N+1):
        if visited[idx] == max(visited):
            tmp.append(idx)
    return max(tmp)

T = 10
for tc in range(1, T+1):
    N, s = map(int, input().split())
    adjLst = [[] for _ in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(0, N, 2):
        adjLst[lst[i]].append(lst[i+1])

    ans = bfs(s)
    print(f'#{tc} {ans}')
'''
24 2 
1 17 3 22 1 8 1 7 7 1 2 7 2 15 15 4 6 2 11 6 4 10 4 2
'''