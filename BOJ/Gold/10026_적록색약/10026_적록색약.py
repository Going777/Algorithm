# from collections import deque
# import sys
# sys.stdin.readline = sys.stdin.readline

# def bfs(i, j, c):
#     q = deque()

#     q.append([i, j])

#     while q:
#         i, j = q.popleft()
#         for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#             ni = i + di ; nj = j + dj
#             if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == c:
#                 q.append([ni, nj])
#                 if c in ['B', 'RG']:
#                     arr[ni][nj] = 1
#                 elif c == 'R':
#                     arr[ni][nj] = 'RG'
#                 elif c == 'G':
#                     arr[ni][nj] = 'RG'

# N = int(sys.stdin.readline())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# b_cnt = r_cnt = g_cnt = 0
# for i in range(N):
#     for j in range(N):
#         # 파란색 처리
#         if arr[i][j] == 'B':
#             b_cnt += 1
#             bfs(i, j, 'B')
#             arr[i][j] = 1       # 파란색은 한 번만 처리해주면 되므로, 1로 값 변경(방문처리)
#         # 빨간색 처리
#         elif arr[i][j] == 'R':
#             r_cnt += 1
#             bfs(i, j, 'R')
#             arr[i][j] = 'RG'    # 적록을 함께 처리해주어야 하기 때문에 'RG'로 값 변경
#         # 초록색 처리
#         elif arr[i][j] == 'G':
#             g_cnt += 1
#             bfs(i, j, 'G')
#             arr[i][j] = 'RG'    # 적록을 함께 처리해주어야 하기 때문에 'RG'로 값 변경

# rg_cnt = 0
# for i in range(N):
#     for j in range(N):
#         # 적록인 경우 처리
#         if arr[i][j] == 'RG':
#             rg_cnt += 1
#             bfs(i, j, 'RG')
#             arr[i][j] = 1

# rgb = r_cnt+g_cnt+b_cnt
# rg_b = rg_cnt+b_cnt
# print(rgb, rg_b)

# '''
# 5
# RGRRB
# GRRRB
# GGGGB
# RRRRR
# GRGGG
# '''

import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]  # .strip()을 추가하여 개행문자 제거
visited = [[0] * N for _ in range(N)]
visited_c = [[0] * N for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(flag, i, j, visited):
    visited[i][j] = 1
    color = arr[i][j]
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # 적록색약인 경우 (R과 G는 동일시)
            if flag:
                if (color in ["R", "G"] and arr[ni][nj] in ["R", "G"]) or arr[ni][nj] == color:
                    dfs(flag, ni, nj, visited)
            
            # 정상인
            else:
                if arr[ni][nj] == color:
                    dfs(flag, ni, nj, visited)

cnt = 0
cnt_c = 0
for i in range(N):
    for j in range(N):
        # 정상인 
        if not visited[i][j]:
            cnt += 1
            dfs(False, i, j, visited)

        # 적록색약인 경우 
        if not visited_c[i][j]:
            cnt_c += 1
            dfs(True, i, j, visited_c)

print(cnt, cnt_c)


# 적록색약이 아닌 사람
# 적록색약인 사람(R == G)