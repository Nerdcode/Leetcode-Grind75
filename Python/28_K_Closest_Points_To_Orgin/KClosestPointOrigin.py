#runtime 653ms. memory 22.21 MB
import heapq

class Solution:
    def kClosest(self, points, k):
        # Let's create a max-heap to store the k closest points based on distance.
        # We're going to make it max-heap friendly by storing negative distances.

        max_heap = []

        # Now, let's loop through the points and calculate the squared Euclidean distance.
        # We'll avoid the square root to keep things snappy.

        for point in points:
            x, y = point
            distance = x * x + y * y

            # We'll push the distance to the heap with a negative sign.
            heapq.heappush(max_heap, (-distance, point))

            # If our heap has more than k points, we'll pop the one with the largest distance.
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Now that we've collected our k closest points, let's reverse the order to get them
        # in ascending order of distance.

        closest_points = [point for (_, point) in max_heap][::-1]

        # And there you have it! The k closest points.

        return closest_points

# Let's try it out with an example:
points = [[1, 3], [-2, 2]]
k = 1
solution = Solution()
result = solution.kClosest(points, k)
print(result)  # Ta-da! The closest point is: [[-2, 2]]
