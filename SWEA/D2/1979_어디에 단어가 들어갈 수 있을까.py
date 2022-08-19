T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())  # 크기 / 단어 길이
    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [
        [0] * (N + 2)]  # 0으로 행렬 둘러쌈
    cnt = 0

    for _ in range(2):  # 원래 행렬 & 전치 행렬 행 탐색
        for i in range(N + 2):  # 원래 행렬에서 앞,뒤로 2개씩 늘었기 때문에 N+1까지 탐색해야 함
            tmp = 0  # 1의 누적합 저장 변수
            for j in range(N + 2):
                if arr[i][j] == 1:  # 해당 원소값이 1인 경우
                    tmp += 1
                else:  # 해당 원소값이 0인 경우
                    if tmp == K:  # 지금까지 누적된 tmp값이 K와 같다면 cnt += 1
                        cnt += 1
                    tmp = 0  # tmp 초기화
        arr = list(map(list, zip(*arr)))  # 행렬 전치하여 열에도 같은 작업 반복

    print(f"#{t} {cnt}")