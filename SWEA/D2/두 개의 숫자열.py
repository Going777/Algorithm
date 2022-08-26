T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: A배열 길이 / M: B배열 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A배열의 길이가 더 짧도록 통일 (N<M)
    if N > M:
        N, M = M, N
        A, B = B, A

    mx_sm = 0
    for j in range(M-N+1):
        tmp_sm = 0
        for i in range(N):
            tmp_sm += A[i] * B[i+j]
        # 최댓값 찾기
        if mx_sm < tmp_sm:
            mx_sm = tmp_sm

    print(f"#{tc} {mx_sm}")