def select_sort(arr, N, K): # 내림차순 반환 (선택정렬)
    for i in range(K): # K번 반복하면 K번째까지의 최대값을 앞쪽부터 찾을 수 있다
        m_idx = i
        for j in range(i+1, N):
            if arr[m_idx] < arr[j]:
                m_idx = j
        arr[m_idx], arr[i] = arr[i], arr[m_idx]
    return arr

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    s_scores = select_sort(scores, N, K)
    k_sum = sum(s_scores[:K])
    print(f"#{t} {k_sum}")
