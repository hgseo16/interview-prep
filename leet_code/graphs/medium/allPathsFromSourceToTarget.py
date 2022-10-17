class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS Solution
        last_node = len(graph) - 1

        # Using queue as I am going to use BFS iteratively
        queue = [[0]]
        result = []
        
        while queue:
            curr = queue.pop(0)
            if curr[-1] is last_node: 
                result.append(curr)
            else:            
                for neighbor in graph[curr[-1]]:
                    queue.append(curr + [neighbor])        
                    
        return result


# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         # BFS Solution
#         last_node = len(graph) - 1

#         # Using stack as I am going to use BFS iteratively
#         stack = [[0]]
#         result = []
        
#         while stack:
#             curr = stack.pop()
            
#             if curr[-1] is last_node:
#                 result.append(curr)
#             else:
#                 for neighbor in graph[curr[-1]]:
#                     stack.append(curr+[neighbor])
        
#         return result