# 방의 크기 N과 방의 구조가 주어졌을 때, 
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하라
# 2칸 이상의 빈 칸이 존재하면 누울 수 있는 곳!!

import sys

N = int(sys.stdin.readline())    # 방 크기
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]   # X는 짐이 있는 곳
result = 0

def check(i, j):
    while (i < N-1) and (j < N-1):
        if (arr[i][j] == '.'):
            if (arr[i+1][j] == '.'):
                result += 1
                j += 1
            if (arr[i][j+1] == '.'):
                result += 1
                i += 1 

check(0, 0)