class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        res=0
        if len(nums)==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]==nums[i+1]:
                res=max(res,count)
                continue 
            else:
                count=1
            res=max(res,count)
        return res
                
            