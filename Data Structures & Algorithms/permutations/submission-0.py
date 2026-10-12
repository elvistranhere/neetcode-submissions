class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = [False]*len(nums)
        res = []
        def dfs(i,sub):
            if i == len(nums):
                res.append(sub)
                return
            for n in range(len(nums)):
                if not picked[n]:
                    picked[n] = True
                    dfs(i+1,sub+[nums[n]])
                    picked[n] = False
        dfs(0,[])
        return res