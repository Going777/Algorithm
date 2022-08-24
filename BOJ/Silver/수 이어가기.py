# N = int(input())
# ans = 0
# ans_lst= []
#
# for n in range(N//2, N+1):      # N의 절반부터 N까지 검사 (N-1까지만 검사하면 반례 1 존재)
#     arr = [N]
#     arr.append(n)
#     i = 1
#     while True:
#         tmp = arr[i-1] - arr[i] # 다음 원소의 값은 전전값에서 전값 뺀 값
#         if tmp < 0:             # 해당 값이 음수라면
#             leng = len(arr)     # 지금까지의 배열 길이를 저장하고 종료
#             break
#         arr.append(tmp)         # 음수가 아니라면 배열에 추가하고 인덱스 +1
#         i += 1
#     # 최대 길이 찾기
#     if ans < leng:
#         ans = leng
#         ans_lst = arr
#
# print(ans)
# print(*ans_lst)