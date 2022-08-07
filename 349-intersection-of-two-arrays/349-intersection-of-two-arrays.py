class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()
        for ele in nums1:
            if ele in nums2:
                res.add(ele)
        return list(res)