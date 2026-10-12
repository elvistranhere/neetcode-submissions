class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(index,sub):
            if index == len(nums):
                res.append(sub)
                return
            dfs(index+1,sub+[nums[index]])
            dfs(index+1,sub)
        dfs(0,[])
        return res
        