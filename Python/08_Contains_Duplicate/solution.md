## Explanation of `containsDuplicate` Function

This function checks if a list of integers `nums` contains any duplicate elements.

1. Convert `nums` into a set to automatically remove duplicates.
2. Compare the length of the set with the length of the original list.
3. If the lengths are different, return `True`, indicating duplicates.
4. If the lengths are the same, return `False`, indicating no duplicates.

Example Usage:
```python
solution = Solution()
nums1 = [1, 2, 3, 4, 5]
result1 = solution.containsDuplicate(nums1)  # Returns False (no duplicates).

nums2 = [1, 2, 3, 1, 4]
result2 = solution.containsDuplicate(nums2)  # Returns True (contains duplicates).