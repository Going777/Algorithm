def my_sort(lst):
    N = len(lst)
    for i in range(N-1):
        mn_idx = i
        for j in range(i+1, N):
            if lst[mn_idx] > lst[j]:
                mn_idx = j
        lst[mn_idx], lst[i] = lst[i], lst[mn_idx]
    return lst

def dfs(s):
    visited = [0]*(N+1)
    stack = []

    visited[s] = 1
    dfs_result.append(s)

    while True:
        for t in adjLst[s]:
            if not visited[t]:
                stack.append(s)

                s = t
                visited[s] = 1
                dfs_result.append(s)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break

def bfs(s):
    visited = [0]*(N+1)
    q = []

    q.append(s)
    visited[s] = 1

    while q:
        i = q.pop(0)
        bfs_result.append(i)

        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = 1


N, M, V = map(int, input().split())     # N: 정점 개수 / M: 간선 개수 / V: 탐색 시작 정점
adjLst = [[] for _ in range(N+1)]
dfs_result = []
bfs_result = []
# 연결리스트 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

for lst in adjLst:                      # 정점 번호가 작은 것을 먼저 방문하기 때문에 연결리스트를 오름차순으로 정렬 필요
    my_sort(lst)

dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)