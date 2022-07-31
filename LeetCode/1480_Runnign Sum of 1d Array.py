# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for idx in range(len(nums)):
            result.append(sum(nums[:idx+1]))
            
        return result
