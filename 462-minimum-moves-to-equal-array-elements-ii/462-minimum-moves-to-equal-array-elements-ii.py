class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        med = nums[len(nums)//2]
        for i in nums:
            res += abs(med-i)
        return res