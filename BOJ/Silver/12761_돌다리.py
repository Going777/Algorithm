import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    # 이동과정에서 100000보다 크거나 0보다 작은 번호는 없다
    visited = [0] * 100001

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        if i == M:
            return visited[i] - 1
        for k in range(8):
            # +- 이동
            if k < 6:
                ni = i + d[k]
                if 0 <= ni < 100001 and not visited[ni]:
                    q.append(ni)
                    visited[ni] = visited[i] + 1
            # 배수 이동
            else:
                ni = i * d[k]
                if 0 <= ni < 100001 and not visited[ni]:
                    q.append(ni)
                    visited[ni] = visited[i] + 1
    return -1   # 도달하지 못한 경우(이번 문제에서는 없어도 괜춘)

A, B, N, M = map(int, input().split())  # A, B: 스카이콩콩 힘 / N: 동규 위치 / M: 주미 위치
# 1만큼 좌우 이동 가능 // A나 B만큼 좌우 이동 가능 // 현 위치의 A배, B배 위치로 이동 가능
d = [-1,1,-A,A,-B,B,A,B]

ans = bfs(N)
print(ans)