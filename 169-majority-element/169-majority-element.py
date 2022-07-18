class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for n in nums:
            if n not in res:
                res[n] = 0
            res[n] += 1
        
        for k, v in res.items():
            if v > len(nums) / 2:
                return k