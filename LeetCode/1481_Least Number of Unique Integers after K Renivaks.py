from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        # arr이 빈 경우 0을 반환
        if not arr:
            return 0 
        
        # arr의 요소별로 카운팅한 값을 키의 값으로 하는 count_arr 생성 & value를 기준으로 오름차순 정렬
        count_arr = sorted(Counter(arr).values())
        
        target = 0
        result = len(count_arr)
        # count_arr를 순회하다가 각 요소의 합이 k이상이 되면 멈추고 뒤에 남은 요소의 갯수 반환
        for idx, cnt in enumerate(count_arr):
            target += cnt
            if target >= k:
                if target == k: # k개와 일치하면 요소가 다 사라지는 것이기 때문에 1을 더 빼줌
                    result -= 1
                result -= idx 
                
                return result
