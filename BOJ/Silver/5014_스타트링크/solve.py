import sys
from collections import deque
input = sys.stdin.readline

# F층으로 이루어진 고층 건물
# G층: 스타트링크 있는 곳
# S층: 강호가 있는 곳
# G층으로 이동하려고 한다
# U: 위층으로 몇 칸
# D: 아래층으로 몇 칸

def bfs(v):
    visited = [0] * (F+1)
    visited[v] = 1
    q = deque([v])

    while q:
        i = q.popleft()
        if (i == G):
            return visited[G] - 1

        for k in (U, -D):
            ni = i + k

            if (0 < ni <= F and not visited[ni]):
                visited[ni] = visited[i] + 1
                q.append(ni)
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
lst = [0] * (F+1)
print(bfs(S))