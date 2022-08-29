T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N: 수강생 수 / K: 과제 제출한 사람 수
    submit = list(map(int, input().split()))    # 제출한 사람 번호 K개
    total = list(range(1, N+1))
    result = []

    for idx in total:
        if idx not in submit:
            result.append(idx)

    print(f"#{tc}", *result)

'''
2
5 3
2 5 3
7 2
4 6
'''