class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        ans = -1e5
        for i in range(len(nums)):
            curSum += nums[i]
            ans = max(curSum, ans)
            if curSum < 0:
                curSum = 0 
        return ans