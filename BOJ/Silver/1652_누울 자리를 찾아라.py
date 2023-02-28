# 방의 크기 N과 방의 구조가 주어졌을 때, 
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하라
# 2칸 이상의 빈 칸이 존재하면 누울 수 있는 곳!!

import sys

N = int(sys.stdin.readline())    # 방 크기
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]   # X는 짐이 있는 곳
t_arr = [list(x) for x in zip(*arr)]
def check(arr):
    result = 0
    for row in arr:
        cnt = 0
        for i in range(len(row)):
            if row[i] == '.':
                cnt += 1
            elif row[i] == 'X':
                cnt = 0
            if cnt == 2:
                result += 1
                # break
                # 벽을 기준으로 좌우 2개 이상씩 빈칸이 있다면 누을 곳이 2개인 것!!!!!!
                # break 없어져야 함!
    return result

print(check(arr), check(t_arr))