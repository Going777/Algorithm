'''
약품 칠해진 셀(테두리)에 도착하면 미생물 절반으로 줄어듬 & 이동방향 반대로
    ㄴ 미생물 수가 홀수면, 미생물 수를 2로 나누고 소수점 버림
    ㄴ 미생물이 한 마리 있다면 > 군집이 사라짐
이동 후 두개의 군집이 한 셀에 모이면 군집들이 합쳐짐 & 이동방향은 미생물 수가 많은 군집 방향으로
M시간 후 남아있는 미생물 수 총합은?
'''
rev_direct = {'1':'2', '2':'1', '3':'4', '4':'3'}
def solve(micros):
    t = 1
    while t <= M:
        for idx, micro in enumerate(micros):
            i, j, m, d = micro
            # 다음 후보지 위치 찾기
            if d == 1: ni=i-1 ; nj=j        # 상
            elif d == 2: ni=i+1 ; nj=j      # 하
            elif d == 3: ni=i ; nj=j-1      # 좌
            else: ni=i ; nj=j+1             # 우
            micro[0] = ni ; micro[1] = nj   # 좌표 업데이트

            if (ni in [0, N-1]) or (nj in [0, N-1]):    # 약품 칠해진 공간에 속한다면
                micro[2] = m // 2                       # 미생물 절반 줄어듬
                if micro[2] == 0:                       # 미생물이 0이라면 군집 삭제
                    micros.pop(idx)
                else:
                    micro[3] = int(rev_direct[str(d)])  # 방향 반대로 업데이트

        micros.sort()
        i = 0; j = i+1
        tmp = [micros[i]]
        while True:
            if i == len(micros)-1:
                break
            if micros[i][0] == micros[j][0] and micros[i][1] == micros[j][1]:
                tmp.append(micros[j])
                j += 1
            else:
                mx = 0 ; sm = 0
                for idx, t in enumerate(tmp):
                    sm += t[2]
                    if t > mx:
                        t = mx
                micros[i][3] = tmp[mx][3]
                micros[i][2] = sm
                j += 1
            if j == len(micros):
                i += 1 ; j = i+1
                tmp = [micros[i]]

            # if micros[i][0] == micros[j][0] and micros[i][1] == micros[j][1]:
            #     tmp.append(micros[j])
            #     j += 1
            #     if micros[i][2] < micros[j][2]:
            #         micros[i][3] = micros[j][3]
            #     micros[i][2] += micros[j][2]
            #     micros.pop(j)
            # else:
            #     j += 1
            #     if j == len(micros):
            #         i += 1 ; j = i+1
        t += 1
    ans = 0
    for micro in micros:
        ans += micro[2]
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M, K, = map(int, input().split())    # N: 행렬 크기 / M: 격리 시간 / K: 미생물 군집 수
    micros = []
    # 세로위치, 가로위치, 미생물 수, 이동방향(상:1, 하:2, 좌:3, 우:4)
    for _ in range(K):
        i, j, m, d = map(int, input().split())
        micros.append([i, j, m, d])
    ans = solve(micros)
    print(f'#{tc} {ans}')

'''
1
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1

1
10 17 46
7 5 724 2
7 7 464 3
2 2 827 2
2 4 942 4
4 5 604 4
7 2 382 1
6 5 895 3
8 7 538 4
6 1 299 4
4 7 811 4
3 6 664 2
6 8 868 2
7 6 859 2
4 6 778 2
5 4 842 3
1 3 942 1
1 1 805 3
3 2 350 3
2 5 623 2
5 3 840 1
7 1 308 4
1 8 323 3
2 3 82 3
2 6 115 2
8 3 930 1
6 2 72 1
2 1 290 3
4 8 574 4
8 5 150 3
8 2 287 2
2 8 909 2
2 7 588 2
7 3 30 3
5 8 655 3
3 8 537 1
4 2 350 3
5 6 199 1
5 5 734 2
3 3 788 1
8 4 893 1
1 4 421 4
6 3 616 2
1 2 556 4
7 8 8 1
5 2 702 2
4 4 503 3
'''