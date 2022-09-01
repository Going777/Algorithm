import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())    # N: 연구소 크기 / M: 바이러스 개수
# 0은 빈 칸, 1은 벽, 2는 바이러스 놓을 수 있는 칸

