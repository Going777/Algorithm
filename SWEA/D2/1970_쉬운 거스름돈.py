T = int(input())
for t in range(1, T+1):
    m = int(input()) # 거슬러줘야 할 돈
    m_u = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 거슬러 줄 수 있는 화폐 단위(내림차순으로 세팅)
    result = []

    for u in m_u:
        result.append(m // u) # 몫의 값 개수만큼 최대로 거슬러 줄 수 있음
        m %= u # 거슬러줘야 할 돈은 나머지 값만큼 남게 됨

    print(f"#{t}")
    print(*result)
