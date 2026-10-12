class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(0,-1)])
        visited = set()
        visited.add(0)
        while q:
            curr,par = q.popleft()
            for nei in adj[curr]:
                if nei == par:
                    continue
                if nei in visited:
                    return False
                q.append([nei,curr])
                visited.add(nei)
        return len(visited) == n
