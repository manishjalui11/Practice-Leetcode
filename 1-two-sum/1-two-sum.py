class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, ele in enumerate(nums):
            t = target - ele
            if t in dic:
                return [i, dic[t]]
            dic[ele] = i