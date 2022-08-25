T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕 크기 / M: 피자 개수
    q = []
    c = list(map(int, input().split()))
    num = list(range(1,M+1))

    C = list(map(list, zip(c, num)))    # [치즈양, 피자번호]가 함께 담긴 리스트
    for _ in range(N):                  # 화덕 크기만큼 피자 투입
        q.append(C.pop(0))

    while q:                            # 화덕이 빌때까지 반복
        cheeze, n = q.pop(0)            # 화덕의 맨 처음 피자 상태 보기
        cheeze //= 2                    # 치즈양 반으로 줄이기
        if cheeze == 0:                 # 꺼낸 피자의 치즈양을 2로나누었을 때 0이라면
            if C:                           # 굽기전 피자가 있다면
                q.append(C.pop(0))          # 화덕에 해당 피자 투입
        else:                           # 0이 아니라면
            q.append([cheeze, n])           # 기존 피자 치즈양 2로 나누어 다시 화덕에 투입

    print(f"#{tc} {n}")                 # 화덕이 비게 될때 그 전에 할당되었던 n이 마지막 피자 번호




'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''

# while len(q) != 1:
#     if q[0][0] == 0:
#         if C:
#             q[0] = C.pop(0)
#         else:
#             q.pop(0)
#
#     tmp = q.pop(0)
#
#     for i in range(len(q)):
#         q[i][0] //= 2
#     tmp = q.pop(0)
#     q.append(tmp)
