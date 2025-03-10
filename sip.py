class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1 
            elif nums[m] < target:
                l = m + 1
        return l
    
a = Solution()
nums = [1,3,5,6]
target = 2
a.searchInsert(nums,target)