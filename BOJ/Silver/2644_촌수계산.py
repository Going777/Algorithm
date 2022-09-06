from collections import deque

def bfs(s):
    visited = [0] * (N+1)
    q = deque()

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        if i == B:
            return visited[i] - 1

        for t in adjLst[i]:
            if not visited[t]:
                q.append(t)
                visited[t] = visited[i] + 1
    return -1

N = int(input())    # 전체 사람 수
A, B = map(int, input().split())    # 촌수 계산해야 하는 두 사람 번호
adjLst = [[] for _ in range(N+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())    # x는 y의 부모 번호
    adjLst[x].append(y)
    adjLst[y].append(x)

ans = bfs(A)
print(ans)

'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''