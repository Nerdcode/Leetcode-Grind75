class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start_color:
                return
            
            image[row][col] = color
            
            dfs(row - 1, col) 
            dfs(row + 1, col)  
            dfs(row, col - 1)  
            dfs(row, col + 1)  
        
        start_color = image[sr][sc]
        dfs(sr, sc)
        return image
