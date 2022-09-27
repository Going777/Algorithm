T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for n in B:
        s = 0       # 탐색 시작 지점(초기화)
        e = N-1     # 탐색 끝 지점(초기화)
        check = 0   # 번갈아 탐색하는지 체크하는 변수 (우측 방문하면 1, 좌측 방문하면 2)
        while s <= e:           # 시작 지점이 끝지점보다 작은 경우에만 반복
            m = (s+e) // 2      # 중간 인덱스
            # 찾고자 하는 값이 A리스트의 중간값보다 크면,
            if A[m] < n:
                if check == 1:  # 체크 변수가 1이라면, 이전에 우측에 방문했다는 뜻이므로
                    break       # 문제 조건과 맞지 않아 종료
                check = 1       # 우측방문 - 1할당
                s = m+1         # 탐색 시작 지점을 중간 인덱스 다음으로
            # 찾고자 하는 값이 A리스트의 중간값보다 작으면,
            elif A[m] > n:
                if check == 2:  # 체크 변수가 2라면, 이전에 좌측에 방문했다는 뜻이므로
                    break       # 문제 조건과 맞지 않아 종료
                check = 2       # 좌측방문 - 2할당
                e = m-1
            # 찾은 경우
            else:
                cnt += 1        # 카운트 + 1
                break

    print(f'#{tc} {cnt}')

'''
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5
'''