import sys
import math
input = sys.stdin.readline

# H*W 크기의 강의실
# 참가자는 세로로 N칸, 가로로 M칸 이상 비우고 앉아야 한다
# 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다
# 최대 몇 명 수용 가능한가?

H, W, N, M = map(int, input().split())

row = math.ceil(W / (M + 1))
col = math.ceil(H / (N + 1))
print(row * col)