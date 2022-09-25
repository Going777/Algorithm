# '''
# 0부터 9까지인 숫자 카드 4세트를 섞고 6개 카드를 고른다
#     연속 숫자가 3개 이상이면 run
#     같은 숫자가 3개 이상이면 triplet
# 플레이어1, 플레이어2가 교대로 한장씩 카드 가져감
# 6개 채우기 전이라도 먼저 run/triplet이 되는 사람이 승자
# '''
#
# def solve(n, lst):
#     if n == N:
#         for i in range(N-2):
#             if (lst[i] == lst[i+1] == lst[i+2]) or (lst[i]+2 == lst[i+1]+1 == lst[i+2]):
#                 return 1
#     for i in range(n, N):
#         lst[i], lst[n] = lst[n], lst[i]
#         chk = solve(n+1, lst)
#         if chk:
#             return 1
#         lst[i], lst[n] = lst[n], lst[i]
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     lst = list(map(int, input().split()))
#     p1_lst = [] ; p2_lst = []
#
#     ans = 0
#     for i in range(0, len(lst), 2):
#         p1_lst.append(lst[i])
#         p2_lst.append(lst[i+1])
#
#         if i >= 4:
#             N = len(p1_lst)
#             p1 = solve(0, p1_lst)
#             if p1:
#                 ans = 1
#                 break
#             p2 = solve(0, p2_lst)
#             if p2:
#                 ans = 2
#                 break
#     print(f'#{tc} {ans}')
#
# '''
# 3
# 9 9 5 6 5 6 1 1 4 2 2 1
# 5 3 2 9 1 5 2 0 9 2 0 0
# 2 8 7 7 0 2 2 2 5 4 0 3
# '''


from collections import deque


def bfs(N, M, si, sj, ei, ej, k):
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    w = ['d', 'l', 'r', 'u']

    result = ''
    q = deque()
    q.append([si, sj, 0, ''])

    while q:
        i, j, dist, word = q.popleft()
        if result and word > result:
            continue
        if dist == k and (i == ei and j == ej):
            if not result:
                result = word
            else:
                return word
        elif dist > k:
            break
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if not result:
                    q.append([ni, nj, dist + 1, word + w[d]])
                else:
                    if word < result:
                        q.append([ni, nj, dist + 1, word + w[d]])
    return 'impossible'


def solution(n, m, x, y, r, c, k):
    result = bfs(n, m, x - 1, y - 1, r - 1, c - 1, k)

    # if not result:
    #     result = 'impossible'
    return result
print(solution(3,4,2,3,3,1,5))