
def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])

    visited = set()

    def dfs(r, c):
        if r < 0 or \
           r >= rows or \
           c < 0 or \
           c >= cols or \
           grid[r][c] == 0 or \
           (r, c) in visited:
            return 0

        visited.add((r, c))

        area = 1
        area += dfs(r+1, c)
        area += dfs(r-1, c)
        area += dfs(r, c+1)
        area += dfs(r, c-1)

        return area

    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_area = max(max_area, dfs(r, c))

    return max_area


# 示例
grid = [
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1]
]
print(max_area_of_island(grid))
