def solution(sizes):
    N = len(sizes)
    visited = [False] * N
    answer = 1000 * 1000

    def dfs(n, mx_w, mx_h):
        nonlocal answer
        if n == N:
            answer = min(answer, mx_w * mx_h)
            return
        
        for idx, (w, h) in enumerate(sizes):
            if not visited[idx]:
              visited[idx] = True
              dfs(n+1, max(mx_w, w), max(mx_h, h))
              dfs(n+1, max(mx_w, h), max(mx_h, w))
              visited[idx] = False

    dfs(0, 0, 0)

    return answer


# ------------------------------------------------------

def solution(sizes):
    # 각 명함을 가로와 세로 중 작은 값은 가로로, 큰 값은 세로로 정렬
    for i in range(len(sizes)):
        sizes[i].sort()
    
    # 가로의 최대값과 세로의 최대값을 구함
    max_w = max([size[0] for size in sizes])  # 가로의 최대값
    max_h = max([size[1] for size in sizes])  # 세로의 최대값
    
    return max_w * max_h  # 가로 * 세로의 곱을 반환

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])