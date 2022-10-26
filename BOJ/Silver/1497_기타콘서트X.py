'''
최대한 많은 곡을 연주하려고 할 때, 필요한 기타의 최소 개수는?
'''
from itertools import combinations

def solve(n, cnt, s_play):
    global mx_play, mn_cnt
    if mx_play > s_play:
        return
    if mx_play < s_play:
        mx_play = s_play
    if s_play == M:
        mn_cnt = cnt
        return mn_cnt

    if n == N:
        if mx_play == 0:
            return -1
        if mn_cnt > cnt:
            mn_cnt = cnt
        return mn_cnt

    for i in range(N):
        for x in lst[i]:
            visited[x] = 1

        solve(n+1, cnt+1, sum(visited))

        for x in lst[i]:
            visited[x] = 0


N, M = map(int, input().split())    # N: 기타 개수 / M: 곡 개수
lst = [[0] for _ in range(N)]
for i in range(N):
    guitar, is_play = input().split()
    tmp = []
    for j in range(M):
        if is_play[j] == 'Y':
            tmp.append(j)
    lst[i] = tmp

mx_play = 0
mn_cnt = 10
visited = [0]*M
solve(0, 0, 0)

print(mn_cnt)