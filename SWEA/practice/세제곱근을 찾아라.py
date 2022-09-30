'''
양의 정수 N에 대해 N=X^3가 되는 양의 정수 X를 구하여라
1 <= N <= 10^18
'''
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     ans = -1
#     for i in range(int(N**(1/3))+1, int(N**(1/3))-1, -1):
#         if i**3 == N:
#             ans = i
#             break
#     print(f'#{tc} {ans}')

# 이진탐색 풀이 방법
# 큰 값이 나오면 이진탐색을 고려해보라
ans = -1
N = int(input())
s = 1; e = N
while s <= e:
    m = (s+e)//2
    if m**3 == N:   # 찾은 경우
        ans = m
        break
    elif m**3 < N:  # 오른쪽
        s = m+1
    else:
        e = m-1     # 왼쪽
'''
3
27
7777
64
'''