from collections import deque

def bfs(i):
    q = deque()

    q.append(i)
    visited[i] = 1

    while q:
        i = q.popleft()
        ni = arr[i]
        if not visited[ni]:
            q.append(ni)
            visited[ni] = 1

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(cnt)

'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''