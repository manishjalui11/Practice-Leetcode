class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = []
        for ele in accounts:
            s.append(sum(ele))
        return max(s)