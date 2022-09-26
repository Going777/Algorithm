'''
사각형 모향을 그리며 다시 출발점으로 돌아오는 경우, 가장 많은 종류의 디저트 수 출력
'''
di = [1,1,-1,-1]
dj = [-1,1,1,-1]
def solve(n, ci, cj, visited):
    global ans
    # 가지치기
    if n == 2 and ans >= len(visited)*2:    # 절반을 왔는데, *2해도 ans보다 작은 경우 > 갱신할 가능성이 없다(non-promising)
        return
    # 종료 조건
    if n > 3:
        return
    # 정답처리
    if n == 3 and (ci, cj) == (si, sj):
        ans = max(ans, len(visited))
    # 하부함수 호출
    for k in range(n, min((n+2),4)):
        ni = ci + di[k] ; nj = cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in visited:
            # 1번 방식
            solve(k, ni, nj, visited+[arr[ni][nj]])
            # 2번 방식 >> 더 빠르다?
            # visited.append(arr[ni][nj])
            # solve(k, ni, nj, visited)
            # visited.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    for si in range(N-2):
        for sj in range(1, N-1):
            solve(0, si, sj, [])

    print(f'#{tc} {ans}')