import sys
sys.stdin = open('input.txt', 'r')

def dfs(s, g):                                      # s는 출발점 / g는 도착점
    visited[s] = 1                                  # 방문표시 (초기화)
    while True:
        for e in range(1, V+1):
            if arr[s][e] == 1 and visited[e] == 0:  # 현재 위치와 연결되어 있고 방문하지 않았다면
                if e == g:                          # 만약 해당 방문예정 지점이 도착점이라면 경로가 존재하는 것 > 함수 종료
                    return 1
                stack.append(s)                     # 현재 지점을 스택에 넣어 다시 되돌아갈 수 있는 발판을 만들고
                s = e                               # 현재 지점을 다음 방문예정 지점으로 이동
                visited[s] = 1                      # 방문표시
                break
        else:                                       # 더이상 연결되어 방문할 곳이 존재하지 않는다면
            if stack:                               # 스택이 비지 않았다면
                s = stack.pop()                     # 스택의 마지막 원소 지점으로 되돌아가 다시 탐색
            else:                                   # 스택이 비었다면
                return 0                            # 종료(끝까지 탐색 완료한 것)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    # 연결리스트 행렬 형태로 받기
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a][b] = 1                               # 단방향 주의!!
    s, g = map(int, input().split())
    visited = [0] * (V+1)                           # 방문 여부 체크
    stack = []                                      # 방문할 곳이 없다면 다시 되돌아갈 정점 모임

    result = dfs(s, g)

    print(f"#{t} {result}")