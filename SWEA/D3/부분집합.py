def dfs(n, sm):
    global cnt

    # 가지치기는 제일 위에 작성, 제일 마지막 순서로
    if sm > K:                  # 이미 K값을 초과하여 답을 찾을 가능성이 없다면 종료
        return

    # 종료 조건
    if n == N:
        # 정답 관련 처리
        if sm == K:             # 지금까지의 합이 K와 같다면 cnt + 1
            cnt += 1
        return

    # 하부 함수(n+1) 호출
    else:
        dfs(n+1, sm + lst[n])   # 해당 숫자(n)를 사용하는 경우
        dfs(n+1, sm)            # 해당 숫자(n)를 사용하지 않는 경우


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0

    # # 비트 연산으로 풀이 >> 확장 또는 활용이 쉽지 않다
    # for i in range(1, 1 << N):
    #     sm = 0
    #     for j in range(N):
    #         if i & 1 << j:
    #             sm += lst[j]
    #     if sm == K:
    #         cnt += 1

    # 백트래킹 풀이 (가능한 모든 경우를 펼쳐서 트리로 표현)
    dfs(n=0, sm=0)

    print(f"#{tc} {cnt}")