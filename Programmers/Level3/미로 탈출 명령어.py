# n x m 격자 미로
# 출발지점: S(x,y) / 도착지점: E(r,c)
    # 격자 바깥으로 못나감
    # 도착할때까지 걸리는 거리는 k / 같은 격자 두 번 이상 방문 가능
    # 탈출 경로는 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 함

from collections import deque

# 하/좌/우/상
dir = [(1,0,'d'),(0,-1,'l'),(0,1,'r'),(-1,0,'u')]

def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y-c)
    # k 내에 도달 못하는 경우 먼저 걸러냄
    if dist > k or (k-dist) % 2:
        return 'impossible'

    q = deque()
    q.append([x, y, ""])

    while q:
        i, j, path = q.popleft()
        cnt = len(path)

        # 도착했는데 남은 거리가 홀수면 다시 돌아오기 불가능
        if (i, j) == (r, c) and (k-cnt) % 2:
            return 'impossible'

        if cnt == k and (i, j) == (r, c):
            return path


        for (di, dj, d) in dir:
            ni, nj = i + di, j + dj
            if (1 <= ni <= n) and (1 <= nj <= m):
                q.append([ni, nj, path+d])



print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))