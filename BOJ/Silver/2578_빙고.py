position = [0] * 25                         # 빙고판 위의 숫자 위치 저장
call = []                                   # 사회자가 부르는 숫자 모음
checked = [[0]*5 for _ in range(5)]         # 사회자가 부른 숫자 체크

i = 0
for _ in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        position[row[j] - 1] = [i, j]       # 각 숫자의 빙고판 위 위치 저장 (단, index를 맞춰주기 위해 -1씩)
    i += 1

for _ in range(5):
    call.extend(list(map(int, input().split())))

def isBingo(checked):
    t_checked = list(zip(*checked))         # 열 방향 검사를 위해 전치행렬 만들어 놓음
    b_cnt = 0                               # 5개 모두 1인 선의 개수

    tmp_d1 = 0                              # 대각선 방향 합(\)
    tmp_d2 = 0                              # 대각선 방향 합(/)
    i = 0
    for _ in range(5):
        tmp_row = 0                         # 행 방향 합
        tmp_col = 0                         # 열 방향 합
        for j in range(5):
            tmp_row += checked[i][j]
            tmp_col += t_checked[i][j]
            if i == j:                      # i와 j가 같을 때 대각선 방향 합 계산 가능
                tmp_d1 += checked[j][j]
                tmp_d2 += checked[j][4-j]
        if tmp_row == 5:                    # 행 방향 합이 5라면 b_cnt += 1
            b_cnt += 1
        if tmp_col == 5:                    # 열 방향 합이 5라면 b_cnt += 1
            b_cnt += 1
        i += 1
    if tmp_d1 == 5:                         # 대각선 방향 합이 5라면 b_cnt += 1
        b_cnt += 1
    if tmp_d2 == 5:                         # 대각선 방향 합이 5라면 b_cnt += 1
        b_cnt += 1

    if b_cnt >= 3:                          # b_cnt값이 3이상이라면 빙고
        return True
    return False

for idx, c in enumerate(call):
    i, j = position[c-1]                    # 사회자가 부른 숫자를 기준으로 position에서 해당 숫자 위치 받음
    checked[i][j] = 1                       # checked 판에서 해당 위치 1로 변경
    if idx >= 11:                           # 빙고가 될 수 있는 최소 카운트는 12번 / idx는 0부터 시작하므로 기준이 11보다 클 경우로 설정
        if isBingo(checked):                # 빙고 조건을 만족했다면 몇 번째에 만족했는지 출력하고 종료
            print(idx + 1)
            break






