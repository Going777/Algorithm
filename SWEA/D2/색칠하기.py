T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    result = 0

    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if arr[i][j] != c:                      # 같은 색이 아닐 경우, 해당 좌표 색깔 값만큼 더해줌
                    arr[i][j] += c

    # 1과 2가 겹치면 3 > 좌표값이 3인 개수 구하기
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                result += 1

    print(f"#{tc} {result}")