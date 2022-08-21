import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    k = 2  # 지금은 2칸이지만, 입력받을수 있는 값이라면
    for i in range(k, N - k):
        # mx = max(lst[i - k:i] + lst[i + 1:i + k + 1])
        mx = lst[i-k] # 첫번째 값을 초기값
        for j in range(i-k+1, i+k+1):
            if i != j and mx < lst[j]: # 내 값은 최대값 찾기에서 제외
                mx = lst[j]
        if lst[i] > mx:
            ans += lst[i] - mx
    print(f'#{test_case} {ans}')