# 8X8 모든 칸은 빈 칸 또는 벽 중 하나
# 시작점은 왼쪽 가장 아래 칸 / 도착점은 오른쪽 가장 위 칸
# 1초마다 모든 벽이 아래에 있는 행으로 내려간다 // 내려갈 행이 없다면 벽은 사라진다
# 1초에 상하좌우/대각선 방향으로 움직일 수 있고, 움직이지 않을 수도 있다(이동은 빈 칸으로만)
# 캐릭터가 먼저 이동하고 벽이 이동한다 (벽이 캐릭터가 있는 칸으로 이동하면 더이상 캐릭터는 이동 불가)
# 도착 지점에 도달할 수 있는지 없는지 구하라

from collections import deque
import sys
input = sys.stdin.readline

di = [-1,1,0,0,-1,-1,1,1,0]
dj = [0,0,-1,1,-1,1,-1,1,0]

def bfs(si, sj):
    q = deque()
    q.append([si, sj, 0])

    while q:
        i, j, turn = q.popleft()

        # 9가지 방향으로 탐색(상하좌우/대각선/제자리)
        for k in range(9):
            ni, nj = i+di[k], j+dj[k]
            ## 벽 위치는 본 위치에서 turn만큼 빼줌으로써 이동한 벽의 위치 좌표 출력 가능
            # 탐색하게될 좌표가 범위 내에 있으면서
            # 해당 위치가 벽이 아니고
            # 해당 위치에서 한 칸위에 벽이 있지 않다면(해당 위치로 가게된다면 다음 턴에 이동 불가) 탐색 계속
            if 0 <= ni < 8 and 0 <= nj < 8 and not board[ni-turn][nj] == "#" and not board[ni-turn-1][nj] == "#":
                # 첫 번째 행에 도달하게 되면 무조건 탈출 가능 => return 1
                if (ni-turn) < 0:
                    return 1
                q.append([ni, nj, turn+1])
    return 0

board = [list(input().rstrip()) for _ in range(8)]   # 빈 칸(.) / 벽(#)
print(bfs(7, 0))
