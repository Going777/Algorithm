# 수빈이는 현재 점 N에 있고, 동생은 점 K에 있다.
# 수빈이의 위치가 X일 때, 걷는다면 1초 후에 X-1 or X+1로 이동한다
# 순간이동을 한다면 1초 후 2*X 위치로 이동한다
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은 몇 초 후인가?

import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    visited = [0]*100001

    while q:
        i = q.popleft()
        if i == K:
            return visited[i]

        # 갈 수 있는 경로를 모두 탐색
        for ni in (i-1, i+1, i*2):
            if 0 <= ni < 100001 and not visited[ni]:
                q.append(ni)
                visited[ni] = visited[i] + 1


N, K = map(int, input().split())

# 수빈이가 동생 위치보다 큰 경우(뒤로 갈 수 있는 경우는 -1밖에 없음) => 두 거리의 차만큼이 가장 빠른 시간
if  N >= K:
    print(N-K)
# 위 경우에 해당되지 않는다면 bfs를 통해 가장 최정의 루트를 찾아야 함
else:
    print(bfs(N))