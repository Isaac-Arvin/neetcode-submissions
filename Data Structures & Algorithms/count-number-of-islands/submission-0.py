class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def visit_adjacent_islands_bfs(r, c):
            q = collections.deque()
            q.append([r, c])
            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if (nr, nc) not in visited and nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    visit_adjacent_islands_bfs(r, c)
                    num_islands += 1

        return num_islands