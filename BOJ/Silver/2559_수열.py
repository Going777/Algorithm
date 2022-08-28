N, K = map(int, input().split())    # N: 수열 길이 / K: 연속 날짜 수(조건)
arr = list(map(int, input().split()))

# 누적합 계산
# acc_sm = [0]
# for idx in range(N):
#     acc_sm.append(acc_sm[idx] + arr[idx])
#
# ans = acc_sm[K] - acc_sm[0]
# for idx in range(K+1, N+1):
#     tmp = acc_sm[idx] - acc_sm[idx-K]
#     if ans < tmp:
#         ans = tmp

ans = sum(arr[:K])
sm = ans
for idx in range(N-K):
    sm = sm - arr[idx] + arr[idx+K]     
    if ans < sm:
        ans = sm

print(ans)

'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3

10 5
3 -2 -4 -9 0 3 7 13 8 -3
'''