class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for i, room in enumerate(rooms):
            graph[i] = []
            for key in room:
                graph[i].append(key)
                
        stack = [0]
        visited = [False]*len(rooms)
        
        while stack:
            curr = stack.pop()
            visited[curr] = True
            for neighbor in graph[curr]:
                if visited[neighbor] == False:
                    stack.append(neighbor)
                    visited[neighbor] = True
            if graph[curr] == []:
                visited[curr] = True
                
        if False in visited:
            return False
        return True
