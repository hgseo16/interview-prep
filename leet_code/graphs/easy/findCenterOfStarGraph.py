from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for key in graph:
            if len(graph[key]) > 1:
                return key
