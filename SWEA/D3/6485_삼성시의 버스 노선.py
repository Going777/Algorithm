T = int(input())
for t in range(1, T + 1):
    N = int(input())
    counts = [0] * 5000  # 정류장별 노선 개수 저장 배열
    result = []  # 최종 결과 저장 배열 (P의 개수만큼 해당 정류장 번호의 노선 개수 저장)

    # start 번호부터 end 번호까지 정류장에 노선 개수 1씩 증가
    for _ in range(N):
        start, end = map(int, input().split())
        counts[start - 1: end] = list(map(lambda x: x + 1, counts[start - 1: end]))

    P = int(input())
    # 각 정류장 번호에 해당하는 노선 개수 result에 추가
    for j in range(1, P + 1):
        result.append(counts[j - 1])

    print(f"#{t}", *result)