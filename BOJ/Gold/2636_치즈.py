'''
치즈가 놓여있으면 1, 안놓여있으면 0
제일 바깥에는 치즈 놓이지 않음
치즈를 공기 중에 놓으면 녹게되는데, 공기와 접촉된 칸은 한 시간이 지나면 녹아 사라진다(가장자리만 녹는다)
    단, 치즈의 구멍을 둘러싼 치즈는 녹지 않는다
공기 중에서 치즈가 모두 녹아 없어지는데 걸리는 시간은?
녹기 한 시간 전 남아있던 치즈량은?
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    vistied = [[0]*M for _ in range(N)]
    q.append([i, j])
    vistied[i][j] = 1
    cnt = 0     # 녹은 치즈량

    while q:
        i, j = q.popleft()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = i +di ; nj = j + dj
            if 0<=ni<N and 0<=nj<M and not vistied[ni][nj]:
                # 공기라면 계속해서 탐색
                if arr[ni][nj] == 0:
                    q.append([ni, nj])
                    vistied[ni][nj] = 1
                # 치즈라면 탐색 중단
                else:
                    arr[ni][nj] = 0         # 다음 번 탐색을 위해 공기로 바꿔줌
                    cnt += 1                # 치즈량 + 1
                    vistied[ni][nj] = 1     # 방문 표시

    result.append(cnt)                      # 해당 턴에서 최종 치즈량 result에 추가
    return cnt                              # 해당 턴에서의 치즈량 반환

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []
time = 0
# 매 시간마다 (0,0)에서 탐색 시작
while bfs(0,0):         # 반환된 치즈량이 있을 때까지 반복(0이라면 치즈가 모두 녹은 것)
    time += 1

print(time)
print(result[-2])       # 녹기 한 시간 전 치즈량을 출력해야하므로, 뒤에서 2번째 원소 출력