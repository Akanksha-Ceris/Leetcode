class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n= len(nums)
    
        sum = 0
        for i in range(len(nums)):
            sum  += nums[i]
        leftsum = 0
        rightsum = 0
        split = 0
        for i in range(n-1):
            leftsum += nums[i]
            rightsum = sum-leftsum
            if leftsum >= rightsum:
                split += 1
        return split                
        