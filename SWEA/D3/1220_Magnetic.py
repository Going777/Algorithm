import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] in [1,2]:
                check.append([arr[i][j], i, j])

    for c, si, sj in check:
        i = si; j = sj

        # 1이면 아래로 이동
        if c == 1:
            while True:
                if i == N-1:
                    arr[i][j] = 0
                    break
                ni = i + 1
                if arr[ni][j] == 0:
                    arr[i][j] = 0
                    i = ni
                    arr[i][j] = c
                else:
                    break
            continue

        # 2면 위로 이동
        elif c == 2:
            while True:
                if i == 0:
                    arr[i][j] = 0
                    break
                ni = i - 1
                if arr[ni][j] == 0:
                    arr[i][j] = 0
                    i = ni
                    arr[i][j] = c
                else:
                    break
            continue

    cnt = 0
    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == 1 and arr[i+1][j] == 2:
                cnt += 1

    print(f"#{tc} {cnt}")




'''
1
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 2 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''
