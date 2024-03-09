class SimpleDAG:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end):
        # 确保起点和终点都存在于图中
        if start not in self.graph or end not in self.graph:
            print(f"无法添加边 {start} -> {end}：起点或终点不存在。")
            return False
        # 检查添加这条边是否会形成环
        if self.does_edge_create_cycle(start, end):
            print(f"无法添加边 {start} -> {end}：会形成环。")
            return False
        # 添加边
        self.graph[start].append(end)
        print(f"边 {start} -> {end} 已成功添加。")
        return True

    def does_edge_create_cycle(self, start, end):
        # 使用DFS来检查添加这条边是否会形成环
        visited = set()

        # DFS遍历来检查是否存在从end到start的路径，如果存在，则添加这条边会形成环
        def dfs(node):
            if node == start:
                return True
            if node in visited:
                return False
            visited.add(node)
            for neighbour in self.graph.get(node, []):
                if dfs(neighbour):
                    return True
            return False

        return dfs(end)


# 示例代码
dag = SimpleDAG()
dag.add_node("A")
dag.add_node("B")
dag.add_node("C")
dag.add_edge("A", "B")  # 成功
dag.add_edge("B", "C")  # 成功
dag.add_edge("C", "A")  # 应该失败，因为形成环
dag.add_edge("C", "D")  # 因为"D"不存在，应该失败
