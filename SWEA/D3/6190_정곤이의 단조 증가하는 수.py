T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = -1
    for i in range(1, N-1):
        for j in range(i+1, N):
            tmp = arr[i] * arr[j]

            s_tmp = str(tmp)
            if len(s_tmp) == 1 and ans == -1:
                ans = tmp
            for k in range(1, len(s_tmp)):
                if s_tmp[k-1] > s_tmp[k]:
                    break
            else:
                ans = max(ans, tmp)

    print(f"#{tc} {ans}")

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     A = list(map(int, input().split()))
#     ans = -1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             a = A[i] * A[j]
#             top_m = 9 # a의 맨뒷자리를 확인할 초기값
#             while a > 0:
#                 if a%10 > top_m:
#                     break
#                 else:
#                     top_m = a%10
#                     a //= 10
#             else:
#                 if A[i] * A[j] > ans:
#                     ans = A[i] * A[j]
#     print(f'#{t} {ans}')

'''
2
4
2 4 7 10
4
2 4 7 10
'''