w, h = map(int, input().split())    # w: 가로 / h: 세로
N = int(input())                    # N: 상점 개수
corr = []
# 남서쪽 모서리를 기준으로 x축 방향으로 일자로 편다고 생각
for _ in range(N+1):                    # 맨 마지막 원소에는 시작점이 들어가게 될 것
    d, y = map(int, input().split())    # d: 방향 / y: 얼마나 떨어져 있는지
    if d == 1:                  # 북
        corr.append(2*w+h-y)
    elif d == 2:                # 남
        corr.append(y)
    elif d == 3:                # 서
        corr.append(2*w+h+y)
    else:                       # 동
        corr.append(w+h-y)

tot = 2*(w+h)
ans = 0
for i in range(N):
    val = abs(corr[i] - corr[-1])           # 시작점과 상점 위치와의 거리 측정
    r_val = tot-val                         # 반대로 측정했을 때의 거리
    ans += val if val < r_val else r_val    # 더 짧은 거리를 ans에 합
print(ans)

'''
10 5
3
1 4
3 2
2 8
2 3
'''