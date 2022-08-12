import copy
T = 10
for _ in range(T):
    t = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    s_j = [idx for idx in range(N) if arr[0][idx] == 1] # 시작 위치 찾기(배열의 첫 행에서 원소값이 1인 모든 인덱스)
    min_dist = 100*100 # 최소 거리
    result = 0

    for jdx in s_j: # 시작 위치 모두 순회하며 찾기
        i = 0 # 시작 위치(행) 초기화
        j = jdx # 시작 위치(열)
        tmp_arr = copy.deepcopy(arr) # 배열 초기화
        dist = 0 # 각 시도 마다의 거리
        while i < N:
            tmp_arr[i][j] = 2 # 왔던 길 표시
            dist += 1
            for k in [-1, 1]: # 좌우로 갈 수 있는지 탐색
                nj = j + k
                if (0 <= nj < N) and (tmp_arr[i][nj] == 1): # 좌우로 갈 수 있다면
                    j = nj # 열 위치 갱신
                    break
            if j != nj: # 열 위치 갱신이 안된경우(좌우로 못가는 경우) > 아래로 이동
                i += 1

        if dist < min_dist: # 각 시도를 끝낼때마다 최소거리 비교
            min_dist = dist
            result = jdx

    print(f"#{t} {result}")
