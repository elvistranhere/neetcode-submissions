class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = [False] * n
        
        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                for i in adj[node]:
                    if not visit[i]:
                        visit[i] = True
                        q.append(i)
        res = 0
        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                bfs(i)
                res +=1
        return res