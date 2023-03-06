# 격자판의 각 점은 두 정수의 쌍 (x,y)로 나타낸다
# 제일 처음 수빈이의 위치는 (xs, yx), 집이 위치한 (xe, ye)로 이동하려 한다
# 두 가지 방법으로 이동 가능
    # 1. 점프 - 상하좌우 점프 (1초 걸림)
    # 2. 텔레포트 - 정해진 좌표로 이동 (10초 걸림)
# 집에 갈 수 있는 가장 빠른 시간은?

import sys
input = sys.stdin.readline

def calc_time(lst):
    time = 0
    x, y = xs, ys
    for (x1, y1, x2, y2) in lst:
        time += abs(x1-x) + abs(y1-y) + 10
        x, y = x2, y2
    time += abs(xe-x) + abs(ye-y)
    return time

def dfs(n, lst):
    global ans

    if n == 3:  # 마지막 텔포 사용 시점(종료 시점)
        t = calc_time(lst)
        # 최소값 갱신
        if t < ans:
            ans = t
        return

    for k in range(3):
        if not used[k]:
            used[k] = True                    # 사용 표시
            x1, y1, x2, y2 = telpo_lst[k]     # 사용할 텔포 좌표(출발, 도착)
            dfs(n+1, lst+[(x1, y1, x2, y2)])  # (x1,y1) => (x2,y2)로 이동
            dfs(n+1, lst+[(x2, y2, x1, y1)])  # (x2,y2) => (x1,y1)로 이동
            dfs(n+1, lst)                     # 텔레포트 사용 X
            used[k] = False                   # 사용 표시 제거

xs, ys = map(int, input().split())  # 출발 좌표
xe, ye = map(int, input().split())  # 도착 좌표
telpo_lst = []
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    telpo_lst.append([x1, y1, x2, y2])
used = [False] * 3
ans = abs(xs-xe) + abs(ys-ye)  # 최소 시간(기본값: 출발지점~도착지점)

dfs(0, [])

print(ans)