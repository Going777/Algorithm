# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     m_cnt = 0
#
#     for i in range(N):
#         tmp = 0
#         for j in range(M):
#             if arr[i][j] == 1:
#                 tmp += 1
#                 if m_cnt < tmp:
#                     m_cnt = tmp
#             else:
#                 tmp = 0
#
#     for j in range(M):
#         tmp = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 tmp += 1
#                 if m_cnt < tmp:
#                     m_cnt = tmp
#             else:
#                 tmp = 0
#
#     print(f"#{t} {m_cnt}")


def solve(arr, leng):
    for row in arr:
        for i in range(mx-leng+1):
            if row[i:i+leng] == [1]*leng:
                return True
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N*M
    arr = []
    for _ in range(N):
       arr.append(list(map(int, input().split())))

    t_arr = list(map(list, zip(*arr)))

    ans = 0
    mx = N if N >= M else M
    for leng in range(mx, 1, -1):
        try:
            if solve(arr, leng):
                ans = leng
                break
            if solve(t_arr, leng):
                ans = leng
                break
        except:
            pass

    print(f"#{tc} {ans}")

'''
3
4 3
1 1 1
1 1 1
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1
'''