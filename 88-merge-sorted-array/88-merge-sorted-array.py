class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i, x in enumerate(nums2):
            nums1[m+i]=x
            
        nums1.sort()