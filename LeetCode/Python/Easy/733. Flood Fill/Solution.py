class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        old = image[sr][sc]
        if old == color:
            return image
        q = []
        q.append([sr,sc])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while(len(q)>0):
            r,c = q.pop(0)
            image[r][c] = color
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if(0 <= nr < m and 0 <= nc < n and image[nr][nc] == old):
                    image[nr][nc] = color
                    q.append([nr,nc])
        return image


        