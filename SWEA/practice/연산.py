from collections import deque

di = [2,1,-1,-10]
def bfs(n):
    q = deque()
    visited = [0]*1000001
    q.append(n)
    visited[n] = 1
    while q:
        i = q.popleft()
        if i == M:
            return visited[i]-1
        for k in range(4):
            if k == 0:
                ni = i * di[k]
            else:
                ni = i + di[k]
            if 0<=ni<=1000000 and not visited[ni]:
                q.append(ni)
                visited[ni] = visited[i] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N)
    print(f'#{tc} {ans}')

'''
3
2 7
3 15
36 1007
'''