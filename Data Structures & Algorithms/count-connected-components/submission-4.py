class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            res = x
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        def union(x,y):
            px,py = find(x), find(y)
            if px == py:
                return False
            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]
            return True
        
        res = n
        for u ,v in edges:
            if union(u,v):
                res -=1
        return res  