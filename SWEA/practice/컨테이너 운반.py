T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w_lst = list(map(int, input().split()))     # N개 컨테이너 각 무게
    t_lst = list(map(int, input().split()))     # M개 트력 각 적재용량
    # 트럭당 한 개의 컨테이너 운반 가능
    # 트럭의 적재용량을 초과하는 컨테이너 운반 불가
    # 최대 M대의 트럭이 편도로 한 번만 운행
    # 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다 > 옮겨진 화물의 전체 무게는?
    # 화물을 싣지 못한 트럭이 있을 수도, 남는 화물이 있을 수도 / 컨테이너를 한 개도 못 옮긴다면 0

    mn = min(N, M)
    w_lst = sorted(w_lst, reverse=True)
    t_lst = sorted(t_lst, reverse=True)

    ans = 0
    if t_lst[0] < w_lst[-1]:
        ans = 0
    else:
        visited = [0]*mn
        for t in range(mn):
            for w in range(t, mn):
                if not visited[w] and t_lst[t] >= w_lst[w]:
                    visited[w] = 1
                    ans += w_lst[w]
                    break
    print(f'#{tc} {ans}')

'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''