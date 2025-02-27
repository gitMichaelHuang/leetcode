class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        nums = list(s)
        print(nums)
        return len(s)

a = Solution()
nums = [1,1,2]
print(a.removeDuplicates(nums))
print(nums)