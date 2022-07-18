class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic ={}
        for i, ele in enumerate(numbers):
            t = target - ele
            if t in dic:
                return [dic[t]+1, i+1]
            dic[ele] = i