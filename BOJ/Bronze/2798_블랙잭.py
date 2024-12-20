from itertools import combinations

T, target = map(int, input().split())
card_list = list(map(int, input().split()))
# 리스트에서 3가지 원소를 뽑아 만들 수 있는 모든 조합 저장하기
combination_lists = list(combinations(card_list, 3))
# 조합 내 합을 구하고 내림차순으로 정렬
combination_lists = sorted(list(map(sum, combination_lists)), reverse=True)

# 순회하다가 target값과 같거나 작은 요소 출력
for data in combination_lists:
    if data <= target:
        print(data)
        break

-------------------------------------------------------------------------------------

N, M = map(int, input().split())
arr = list(map(int, input().split()))
           
# list내에서 순회하며 가능한 경우의 수 모두 구하기
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            target = arr[i] + arr[j] + arr[k]
            if target > M:
                continue
            else:
                result = max(result, target)
print(result)
