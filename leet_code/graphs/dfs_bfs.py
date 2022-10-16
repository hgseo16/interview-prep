graph = {
	"a": ['b', 'c'],
	"b": ['d'],
	"c": ['e'],
	"d": ['f'],
	"e": [],
	"f": []
}

def depthFirstPrintIterative(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

print('DFS Iterative')
depthFirstPrintIterative(graph, 'a')
print('-------------------------')

def depthFirstPrintRecursive(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecursive(graph, neighbor)

print('DFS Recursive')
depthFirstPrintRecursive(graph, 'a')
print('-------------------------')

def breadthFirstPrintIterative(graph, source):
    queue = [source]
    while len(queue) > 0:
        # pop(0) is a dequeue
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

print('BFS Iterative')
breadthFirstPrintIterative(graph, 'a')
print('-------------------------')

