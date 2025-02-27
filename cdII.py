class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        for i in range(len(nums)):
            for j in range(0, k):
                if nums[j] == i:
                    return True
        return False

a = Solution()
print(a.containsNearbyDuplicate([1,2,3,1,2,3], 2))