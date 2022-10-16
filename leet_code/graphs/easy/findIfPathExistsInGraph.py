class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
	
def depthFirstPrintIterative(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for edges in graph[current]:
            stack.append(edges)

# def depthFirstPrintRecursive(graph, source):

graph = {
	"a": ['c', 'b'],
	"b": ['d'],
	"c": ['e'],
	"d": ['f'],
	"e": [],
	"f": []
}

depthFirstPrintIterative(graph, 'a')
