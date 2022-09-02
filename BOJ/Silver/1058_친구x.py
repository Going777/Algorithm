from collections import deque

def bfs(s):
    global mx_cnt
    visited = [0]*N
    q = deque()
    cnt = 0

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()

        # depth를 2까지만 제한
        if visited[i]-1 == 2:
            break

        for t in adjLst[i]:
            if visited[t] == 0:
                cnt += 1
                q.append(t)
                visited[t] = visited[i] + 1

    if mx_cnt < cnt:
        mx_cnt = cnt

N = int(input())
adjLst = [[] for _ in range(N)]

arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == "Y":
            adjLst[i].append(j)

mx_cnt = 0
for n in range(N):
    bfs(n)

print(mx_cnt)