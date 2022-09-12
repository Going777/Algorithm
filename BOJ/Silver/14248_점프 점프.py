from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque()
    visited = [0] * (N+1)

    q.append(s)
    visited[s] = 1

    while q:
        i = q.popleft()
        for ni in [i + arr[i], i - arr[i]]: # 현재위치에서 돌에 적힌 번호만큼 좌우 이동 가능
            if 1 <= ni <= N and not visited[ni]:
                q.append(ni)
                visited[ni] = 1
    return sum(visited)

N = int(input())    # 돌 개수(1~N번까지 돌 번호)
arr = [0] + list(map(int, input().split()))   # 각 돌에서 이동할 수 있는 거리
S = int(input())    # 출발점

ans = bfs(S)
print(ans)