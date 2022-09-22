# def solve(n, cnt):
#     global ans
#     # 종료 조건(교환횟수 충족)
#     if cnt == k:
#         # 최댓값 업데이트
#         tmp = int(''.join(lst))
#         ans = max(ans, tmp)
#         return
#     # 하부 함수 호출
#     # 뒤쪽에서 더 크거나 같은 값을 찾아 스왑
#     for i in range(n, N):
#         for j in range(i+1, N):
#             if lst[i] <= lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#                 solve(i, cnt+1)
#                 lst[i], lst[j] = lst[j], lst[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     lst, k = input().split()
#     lst = list(lst) ; k = int(k)
#     N = len(lst)
#
#     ans = 0
#     # 숫자가 내림차순 정렬되어 있는 경우,
#     if lst == sorted(lst, reverse=True):
#         if k%2:     # 교환횟수가 홀수일 때
#             for i in range(N-1):
#                 if lst[i] == lst[i+1]:          # 리스트 내 같은 수가 하나라도 있다면(둘만 반복해서 스왑)
#                     ans = int(''.join(lst))     # ans는 현재 리스트 그대로
#                     break
#             else:                                       # 같은 수가 없다면
#                 lst[-1], lst[-2] = lst[-2], lst[-1]     # 뒷 자리 2개 자리 스왑
#                 ans = int(''.join(lst))
#         else:       # 교환횟수가 짝수일 때
#             ans = int(''.join(lst))     # ans는 현재 리스트 그대로
#     # 그 외 경우,
#     else:
#         solve(0,0)
#     print(f'#{tc} {ans}')

# --------------------------------------------------------------------------------------------

def solve(n):
    global ans
    tmp = int(''.join(lst)) # 호출되는 시점에서의 상금 값

    # 가지치기
    if tmp in visited[n]:   # 해당 횟수에 이미 그 값이 있다면, 함수 리턴(빠른 종료)
        return
    visited[n].append(tmp)  # 해당 값이 없다면 값 추가

    # 종료 조건
    if n == N:
        ans = max(ans, tmp)
        return

    # 하부함수 호출
    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j], lst[i]
            solve(n+1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for tc in range(1, T+1):
    lst, N = input().split()
    N = int(N)
    lst = list(lst)
    L = len(lst)

    ans = 0
    # 숫자가 내림차순 정렬되어 있는 경우,
    if lst == sorted(lst, reverse=True):
        if N%2:     # 교환횟수가 홀수일 때
            for i in range(L-1):
                if lst[i] == lst[i+1]:          # 리스트 내 같은 수가 하나라도 있다면(둘만 반복해서 스왑)
                    ans = int(''.join(lst))     # ans는 현재 리스트 그대로
                    break
            else:                                       # 같은 수가 없다면
                lst[-1], lst[-2] = lst[-2], lst[-1]     # 뒷 자리 2개 자리 스왑
                ans = int(''.join(lst))
        else:       # 교환횟수가 짝수일 때
            ans = int(''.join(lst))     # ans는 현재 리스트 그대로
    # 그 외 경우,
    else:
        visited = [[] for _ in range(N+1)]    # 각 횟수별 얻게되는 상금 저장
        solve(0)
    print(f'#{tc} {ans}')

'''
3
123 1
2737 1
32888 2
'''