# 리스트를 이용
# def quick_sort(lst):
#     # 종료 조건
#     if len(lst) <= 1:
#         return lst
#     # pivot을 기준으로 좌/우로 나눔 (단위작업)
#     pivot = lst.pop()
#     left, right = [], []
#     for n in lst:
#         if n < pivot:
#             left.append(n)
#         else:
#             right.append(n)
#     # 왼쪽 정렬, 오른쪽 정렬, 그 결과를 합쳐서 리턴
#     return quick_sort(left) + [pivot] + quick_sort(right)

# 인덱스를 이용(파이썬 외 언어 사용시 짜야할 코드 흐름) > 조금 더 빠름
def quick_sort2(s, e):
    if s >= e:
        return
    # pivot 기준으로 작은 값 왼쪽, 그 외 오른쪽  (단위작업)
    pivot = e
    tmp = s
    for i in (s, e):
        if lst[i] < lst[pivot]: # pivot 왼쪽으로 이동시켜야 함
            lst[i], lst[tmp] = lst[tmp], lst[i]
            tmp += 1
        lst[pivot], lst[tmp] = lst[tmp], lst[pivot]
        pivot = tmp
    # pivot 기준 왼쪽 정렬 & 오른쪽 정렬 (하부함수 호출)
    quick_sort2(s, pivot-1)     # 왼쪽 정렬
    quick_sort2(pivot+1, e)     # 오른쪽 정렬

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # q_lst = quick_sort(lst)
    q_lst = quick_sort2(0, N-1)
    print(f'#{tc} {q_lst[N//2]}')

'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''