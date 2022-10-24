from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        graph = defaultdict(list)
        
        for str in strs:
            key = ''.join(sorted(str))
            graph[key].append(str)

        result = []
        
        for key in graph:
            result.append(graph[key])
            
        return result
