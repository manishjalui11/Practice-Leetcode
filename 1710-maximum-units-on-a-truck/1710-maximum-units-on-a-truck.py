class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        total_unit = 0
        while boxTypes and truckSize>0:
            box = boxTypes.pop(0)
            amt_taken = min(box[0], truckSize)
            total_unit += amt_taken * box[1]
            truckSize -= amt_taken
        return total_unit