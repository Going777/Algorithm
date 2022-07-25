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
