class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row,col):
            count = 0
            q = deque([(row, col)])
            grid[row][col] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                count += 1
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, bfs(row,col))
        return maxArea
        