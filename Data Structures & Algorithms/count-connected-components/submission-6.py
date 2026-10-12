class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node):
            if visited[node] == True:
                return
            visited[node] = True
            for nei in adj[node]:
                dfs(nei)
        res = 0
        for i in range(n):
            if visited[i] == False:
                res +=1
                dfs(i)
        return res
