class Graph:
    def __init__(self, num_of_vertices):
        self.graph = {i: [] for i in range(num_of_vertices)}
        self.num_of_vertices = num_of_vertices

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def topological_sort_util(self, v, visited, stack):
        # 标记当前节点为已访问
        visited[v] = True
        # 遍历所有邻接节点
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        # 当前节点的所有邻接节点都已被访问，将其推入栈中
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.num_of_vertices
        stack = []

        # 对所有未访问的节点调用递归辅助函数
        for i in range(self.num_of_vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack

# 示例
num_of_vertices = 6
graph = Graph(num_of_vertices)
graph.add_edge(5, 2)
graph.add_edge(5, 0)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

print("拓扑排序结果：")
print(graph.topological_sort())
