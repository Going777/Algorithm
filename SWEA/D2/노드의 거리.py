def bfs(s, g):
    q = []

    visited[s] = 1
    q.append(s)

    while q:
        i = q.pop(0)
        if i == g:                          # 도착점을 찾았다면
            return visited[g]-1             # 해당 도착점의 visited배열의 값 -1 반환
        for t in adjLst[i]:
            if not visited[t]:
                visited[t] = visited[i] + 1
                q.append(t)
    return 0                                # s와 g가 연결되어 있지 않은 경우 0 반환

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjLst = [[] for _ in range(V+1)]
    # 연결리스트 만들기
    for _ in range(E):
        a, b = map(int, input().split())
        adjLst[a].append(b)
        adjLst[b].append(a)
    s, g = map(int, input().split())        # s: 출발정점 

    visited = [0]*(V+1)
    ans = bfs(s, g)

    print(f"#{tc} {ans}")

'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6 
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''