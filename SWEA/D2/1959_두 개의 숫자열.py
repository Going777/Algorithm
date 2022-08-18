import sys
sys.stdin = open('input.txt', 'r')

def check(N, M, a, b):           # N > M 일때로 설정 -> len(a) > len(b)
    global result                # gloabal로 선언함으로써 return하지 않고도 전역변수 변경 가능
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += b[j] * a[i+j]
        if result < tmp:         # 현재 result값보다 크면 업데이트
            result = tmp

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    if N > M:
        check(N, M, a, b)
    else:
        check(M, N, b, a)

    print(f"#{t} {result}")