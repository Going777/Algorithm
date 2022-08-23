# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     num = list(range(1, N+1))                   # 번호 저장 리스트
#
#     for _ in range(N//2):
#         M = len(arr)
#         lose = []
#         for i in range(0, M-1, 2):
#             if (arr[i] % 3)+1 == arr[i+1]:        # 뒷 사람이 이긴 경우
#                 lose.append(i)                  # 앞 사람의 인덱스를 lose 배열에 추가
#             else:                               # 앞 사람이 이기거나 비긴 경우
#                 lose.append(i+1)                # 뒷 사람의 인덱스를 lose 배열에 추가
#
#         for l in lose[::-1]:                    # 진 사람들은 배열에서 삭제
#             arr.pop(l)
#             num.pop(l)
#
#     print(f"#{tc} {num[0]}")                    # 최종 인덱스 배열에 남은 원소가 최종 승리자의 번호


tbl = [0,2,3,1]
def solve(s, e):
    # 종료 조건
    if s == e:
        return s
    # 하부호출 ( 단위 작업: 2등분해서 각각 승자 ->  )
    else:
        a = solve(s, (s+e)//2)      # 앞쪽(왼쪽)에서 승자 구하기
        b = solve((s+e)//2+1, e)    # 뒤쪽(오른쪽)에서 승자 구하기

        if tbl[lst[a]] == lst[b]:   # b가 승리한 경우, b가 승자
            return b
        else:                       # 비기거나 a 승리한 경우, a가 승자
            return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = solve(1, N)    # 1~N 사이의 최종 승리자의 인덱스를 리턴해주는 함수

    print(f"#{tc} {ans}")
'''
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
'''