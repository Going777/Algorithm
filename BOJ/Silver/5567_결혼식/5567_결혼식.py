# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(s):
#     q = deque()
#     visited = [0] * (N+1)
#     cnt = 0

#     q.append(s)
#     visited[s] = 1  # 방문표시와 동시에 depth 표현

#     while q:
#         i = q.popleft()
#         if visited[i]-1 == 2:   # depth를 2까지만 탐색
#             return cnt
#         for t in adjLst[i]:
#             if not visited[t]:
#                 q.append(t)
#                 visited[t] = visited[i] + 1
#                 cnt += 1
#     return cnt

# N = int(input())    # 동기 수(1~N번, 1번은 상근)
# M = int(input())    # 리스트 길이
# adjLst = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     adjLst[a].append(b)
#     adjLst[b].append(a)
# ans = bfs(1)
# print(ans)

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adjLst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjLst[a].append(b)
    adjLst[b].append(a)

def bfs(v):
    global visited
    visited[v] = 1
    q = deque([v])

    while q:
        i = q.popleft()

        if (visited[i] - 1 == 2):
            break

        for t in adjLst[i]:
            if not visited[t]:
                visited[t] = visited[i] + 1
                q.append(t)

bfs(1)
cnt = 0
print("visited", visited)
for i in range(2, N + 1):
    # 친구의 수 : 본인, 본인의 친구, 친구의 친구로 최대 3명까지 카운트 가능
    if 0 < visited[i] < 4:
        cnt += 1
print(cnt)

