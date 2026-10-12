class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minLength = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]: 
                return ""
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visited = {}
        def dfs(char):
            if char in visited: 
                return visited[char]
            visited[char] = True
            for i in adj[char]:
                if dfs(i):
                    return True
            visited[char] = False
            res.append(char)
            return False 
        for c in adj.keys():
            if dfs(c):
                return ""
            
        return "".join(reversed(res))


        