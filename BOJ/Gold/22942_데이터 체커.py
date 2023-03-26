# 만족해야 하는 조건
    # 모든 원의 중심 좌표는 x축 위에 존재해야 함
    # N개의 원 중 임의의 두 원을 선택했을 때, 교점이 없어야 함 (포함관계이거나, 외부관계)

import sys
input = sys.stdin.readline
lst = []
q = []

N = int(input())    # 원의 개수
for _ in range(N):
    x, r = map(int, input().split())    # x: 원의 중심 x좌표 / r: 원 반지름
    lst.append((x-r, x+r))              # 원의 시작점, 끝 점을 계산해서 리스트에 삽입

# x좌표 기준으로 원을 차례로 탐색할 예정 => 정렬 필요
lst.sort()

q.append(lst[0])
for i in range(1, N):
    # 탐색 순서 원의 시작점, 끝점
    s, e = lst[i]

    # 비교 대상 존재(q가 비지 않음)
    # 비교대상이 존재하지만, 탐색 순서의 원의 시작점이 큐 마지막 원소의 끝 점보다 크다면 => 교점X => 고려X
    while q and s > q[-1][1]:
        q.pop()

    if q:
        # 큐 안의 마지막 원소의 시작점, 끝 점
        qs, qe = q[-1]
        # 교점이 생길 수 있는 부분을 찾음 => 찾는다면 문제 조건을 만족 못시킨 것
        if (s == qs) or (s <= qe <= e):
            print("NO")
            exit()

    q.append(lst[i])

print("YES")