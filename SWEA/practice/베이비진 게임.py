'''
0부터 9까지인 숫자 카드 4세트를 섞고 6개 카드를 고른다
    연속 숫자가 3개 이상이면 run
    같은 숫자가 3개 이상이면 triplet
플레이어1, 플레이어2가 교대로 한장씩 카드 가져감
6개 채우기 전이라도 먼저 run/triplet이 되는 사람이 승자
'''

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

# ----------------------------------------------------------------

# [1] cnt1[], cnt2[] 각각 사용자별 획득한 카드 개수 표시
# [2] 카드 추가 후, baby()==1이면 종료
# cnts[i] >= 3 or (cnts[i]>=1) and (cnts[i+1]>=1) and (cnts[i+2]>=1)

def baby(cnts, idx):
    if cnts[idx] >= 3:  # triplet의 경우
        return 1
    for i in range(idx-2, idx+1):
        if (i>=0) and (cnts[i]>=1 and cnts[i+1]>=1 and cnts[i+2]>=1):   # 범위 체크 & run인 경우
            return 1
    return 0

lst = list(map(int, input().split()))
cnt1 = [0]*12
cnt2 = [0]*12
ans = 0

for i in range(len(lst)):
    if i%2:
        cnt2[lst[i]] += 1
        if baby(cnt2, lst[i]):  # cnt2 배열에 추가된 lst[i] 주변을 탐색하기 위해 해당 인덱스 추가
            ans = 1
            break
    else:
        cnt1[lst[i]] += 1
        if baby(cnt1, lst[i]):
            ans = 2
            break
print(ans)

'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''