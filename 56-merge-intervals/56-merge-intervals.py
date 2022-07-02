class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda row: row[0])
        result = [intervals[0]]
        for ele in intervals:
            if ele[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], ele[1])
            else:
                result.append(ele)
        return(result)

