# Flood Fill

Refer this -> [Flood_Fill](https://leetcode.com/problems/flood-fill/)

We are given an image represented by a 2D grid of pixels, where each pixel has a value. We need to perform a flood fill operation on the image, 
starting from a given pixel position i.e `(sr, sc)`.  The flood fill operation involves changing the color of the starting pixel and all the connected pixels 
of the same color.


# Code Explanation

***Approach:***  We gonna use recursive Depth-First-Search(DFS) for this one. We start at the given pixel position (sr, sc) and recursively explore its neighboring 
pixels in the four cardinal directions (up, down, left, and right) to check if they have the same color. If they do, we update their color to the target color 
and continue the flood fill operation on those pixels.

Let's go through the code step by step:

- The floodFill method takes the image, starting row `sr`, starting column `sc` and target color `color` as input.
- We first check if the starting pixel `image[sr][sc]`  already has the same color as the target color. If it does, we return the original image since no
  changes need to be made.
- Next, we define the dfs function, which performs the depth-first search.
- The dfs function takes the current row `row` and column `col` as inputs.
- In the dfs function, we have a base case that checks if the current pixel is out of bounds or has a different color than the starting pixel.
  If either of these conditions is met, we return from the function.
- If the current pixel has the same color as the starting pixel, we update its color to the target color.
- We then make recursive calls to the dfs function for the four neighboring pixels (up, down, left, and right) to continue the flood fill operation.
- Before calling the dfs function, we store the color of the starting pixel in the `start_color` variable for comparison.
- Finally, we call the dfs function with the starting row and column to start the flood fill operation, and then return the modified image.
