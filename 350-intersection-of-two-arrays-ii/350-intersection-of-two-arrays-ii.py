class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 <= l2:
            return self.commonIndex(nums1, nums2)
        elif l1 > l2:
            return self.commonIndex(nums2, nums1)

    def commonIndex(self, shorter: List[int], longer: List[int]) -> List[int]:
        result = []
        dic= {}
        s=set(shorter)
        
        for ele in longer:
            if ele in shorter:
                result.append(ele)
                shorter.remove(ele)
        return result