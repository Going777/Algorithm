import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    if N == 1:
        result = [[1]]
    elif N == 2:
        result = [[1],[1,1]]
    else:
        result = [[1] for _ in range(N)] # 초기화
        result[1].append(1)              # 초기화

        for i in range(2, N): # 2번쨰 행부터 작업
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j]) # 이전 행 원소 2개 합해서 현재 행에 추가
            result[i].append(1) # 현재 행 마지막에는 1 추가

    print(f"#{t}")
    [print(*row) for row in result]
