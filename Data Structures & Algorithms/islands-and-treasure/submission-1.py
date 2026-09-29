class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        visited = {}

        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] + 1 < grid[nr][nc]:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append([nr, nc])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row, col)