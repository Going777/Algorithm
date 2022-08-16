def is_palindrome(arr, N, M):
    for i in range(N):
        k = M-1
        for j in range(N-M+1):
            for k in range(M-1, M//2-1, -1):
                if arr[i][j+M-k-1] != arr[i][j+k]:
                    break
                if k == M//2:
                    return ''.join(arr[i][j:j+M])
    return ''

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N:배열 길이, M:타겟 패턴 길이
    arr = [list(input()) for _ in range(N)]
    result = ''

    for _ in range(2): # 행 방향/ 열 방향 2번 검사 위해
        result = is_palindrome(arr, N, M)
        if len(result): # 행 방향에서 회문을 찾았다면 반복문 중단
            break
        arr = list(map(list, zip(*arr))) # 행/열 전치

    print(f"#{t} {result}")
