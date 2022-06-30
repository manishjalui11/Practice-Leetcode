class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for ele in nums:
            if ele in d:
                return True
            d.add(ele)