'''
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고자 한다
판매 이용권
    1. 1일 이용권
    2. 1달 이용권(매달 1일부터 시작)
    3. 3달 이용권(매달 1일부터 시작)
    4. 1년 이용권(매년 1월 1일부터 시작)
각 이용권의 요금과 각 달의 이용계획을 고려할 때 가장 적게 지출하는 비용은?
'''
T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    m_cost = [0]*13         # 달별 최소 지출 비용
    for n in range(1, 13):
        tmp = [3000, 3000, 3000, 3000]
        # 1일 이용권 구매
        tmp[0] = m_cost[n-1] + lst[n-1]*cost[0]
        # 1달 이용권 구매
        tmp[1] = m_cost[n-1] + cost[1]
        # 3달 이용권 구매
        if n >= 3:
            tmp[2] = m_cost[n-3] + cost[2]
        # 1년 이용권 구매
        if n >= 12:
            tmp[3] = cost[3]
        m_cost[n] = min(tmp)

    print(f'#{tc} {m_cost[12]}')


'''
1
10 40 100 300   
0 0 2 9 1 5 0 0 0 0 0 0
'''