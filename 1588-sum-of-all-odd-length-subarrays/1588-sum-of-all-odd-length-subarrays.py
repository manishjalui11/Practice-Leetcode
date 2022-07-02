class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(len(arr)):
            ss=0
            for j in range(i,len(arr)):
                ss+=arr[j]
                if (i+j)%2==0:
                    s+=ss
        return s
