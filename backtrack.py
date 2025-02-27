class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            print("i = ", i)
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])

            print("Subset: ", subset) # 1

            dfs(i + 1)
            subset.pop()

            print("Subset pop: ", subset) # 2
            
            dfs(i + 1)

        dfs(0)
        return res
    
a = Solution()
nums = [1,2,3]
res = a.subsets(nums)
print(res)