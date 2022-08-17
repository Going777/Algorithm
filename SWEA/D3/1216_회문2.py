import sys
sys.stdin = open('../D2/input.txt', 'r')

# #     for i in range(N):
# #         for j in range(N):
# #             tmp = 0
# #             for k in range(N-1, tmp, -1):
# #                 if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
# #                     tmp += len(arr[i][j:j+k])
# #                     break
# #             if max_len < tmp:
# #                 max_len = tmp
# #     return max_len

def isPalindrome(lst):
    M = len(lst)
    for i in range(M-1, M//2-1, -1): # 입력 받는 리스트의 반만큼만 수행하여 회문인지 검사
        if lst[M-i-1] != lst[i]:
            return False
    return True

T = 10
for _ in range(T):
    t = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    t_arr = list(zip(*arr)) # 전치 행렬
    max_len = 1 # 찾은 회문 문자열의 길이

    for k in range(N, 1, -1): # 가능한 최대길이부터 거꾸로 검사
        if max_len > k: # 현재 찾은 회문 길이가 k보다 크다면 종료 (최대 길이에서 회문을 찾았다면)
            break
        for i in range(N-k+1): # 탐색 행의 인덱스 시작위치
            if max_len == k: # 최대 길이 k만큼의 회문을 찾았다면 종료
                break
            for lst, t_lst in zip(arr, t_arr): # 행/열 방향 동시에 행 탐색 ( 열 방향은 전치하여 행 방향으로 변환 )
                if isPalindrome(lst[i:i+k]) or isPalindrome(t_lst[i:i+k]):
                    max_len = k
                    break

    print(f"#{t} {max_len}")