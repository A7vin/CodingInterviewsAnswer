
class SampleDAG:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end):
        if start == end:
            print("不能添加环")
            return False
        if end in self.graph[start]:
            print("边已存在")
            return True
        if self.has_cycle(start, end):
            print("添加这条边会造成环")
            return False
        self.graph[start].append(end)
        if end not in self.graph:
            self.graph[end] = []
        return True

    def has_cycle(self, start, end):
        visited = set()
        return self._dfs_cycle_check(start, end, visited)

    def _dfs_cycle_check(self, current, target, visited):
        if current in visited:
            return True
