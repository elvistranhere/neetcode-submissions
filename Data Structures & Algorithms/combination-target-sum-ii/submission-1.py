class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index,S,sub):
            if S == target:
               res.append(sub)
               return 
            if index == len(candidates) or S > target:
                return 
            dfs(index+1,S+candidates[index], sub + [candidates[index]]) 
            while index+1 < len(candidates) and candidates[index+1] == candidates[index]:
                index+=1
            dfs(index+1,S, sub) 
        dfs(0,0,[])
        return res
        