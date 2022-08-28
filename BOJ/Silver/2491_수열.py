N = int(input())    # 수열의 총 길이
arr = list(map(int, input().split()))

ans = 0
# 증가할 때 카운트 세기
inc_cnt = 1
for i in range(1, N):
    if arr[i-1] <= arr[i]:
        inc_cnt += 1
    else:
        ans = max(ans, inc_cnt)
        inc_cnt = 1
ans = max(ans, inc_cnt)

# 감소할 때 카운트 세기
dec_cnt = 1
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        dec_cnt += 1
    else:
        ans = max(ans, dec_cnt)
        dec_cnt = 1
ans = max(ans, dec_cnt)

print(ans)