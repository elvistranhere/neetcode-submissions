class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = [False] * n
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                res +=1
        return res