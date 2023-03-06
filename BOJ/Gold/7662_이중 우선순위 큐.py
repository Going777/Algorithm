# 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제
# 두 가지 연산 => 삽입 / 삭제
# 두 가지 삭제 옵션 => 우선 순위 높은 데이터 삭제(1) / 우선 순위 낮은 데이터 삭제(-1)

# 정수만 저장하는 이중 우선순위 큐 Q가 있을 때, 저장되는 값 자체를 우선순위로 간주
# 동일한 정수가 삽입될 수 있다
# 삭제 연산에서 최댓값 또는 최솟값이 둘 이상이라면 하나만 삭제
# Q가 비었는데 삭제 연산을 해야한다면 pass

# 모든 연산 처리 후 Q에 남아있는 값 중 최댓값과 최솟값을 출력하라 / 비었다면 EMPTY

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())    # 입력 데이터 수
for _ in range(T):
    k = int(input())    # Q에 적용할 연산의 개수
    min_heap = []   # 최소힙 배열
    max_heap = []   # 최대힙 배열
    remove_check = [False]*k   # 삭제 여부 판별할 배열
    for idx in range(k):
        op, n = input().split()     # 연산(D-삭제, I-삽입) & 정수 n
        # 삽입 연산
        if op == 'I':
            # 최소힙 / 최대힙 배열 저장 시 삭제 여부를 알 수 있도록 데이터에 인덱스를 함께 저장
            heappush(min_heap, (int(n), idx))
            heappush(max_heap, (-int(n), idx))

        # 삭제 연산
        else:
            # 우선 순위 낮은 데이터 삭제 -> 최소힙에서 삭제
            if n == '-1':
                while min_heap:
                    # 삭제 표시 되지 않은 데이터인 경우
                    if not remove_check[min_heap[0][1]]:
                        remove_check[min_heap[0][1]] = True     # 삭제 표시
                        heappop(min_heap)                       # 힙에서 삭제
                        break                                   # 종료
                    # 삭제 표시된 데이터인 경우
                    else:
                        heappop(min_heap)                       # 힙에서 삭제

            # 우선 순위 높은 데이터 삭제 -> 최대힙에서 삭제
            else:
                while max_heap:
                    if not remove_check[max_heap[0][1]]:
                        remove_check[max_heap[0][1]] = True
                        heappop(max_heap)
                        break
                    else:
                        heappop(max_heap)


    # 삭제 표시되었지만 삭제되지 않은 데이터, 힙에서 실제로 삭제
    while min_heap and remove_check[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and remove_check[max_heap[0][1]]:
        heappop(max_heap)


    if not min_heap and not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

