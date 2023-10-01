class Solution:
    def firstBadVersion(self, n: int) -> int:
        end = n
        start = 0
        while start <= end:
            middle = int((end - start) / 2) + start
            if not isBadVersion(middle):
                start = middle + 1
                continue
            if isBadVersion(middle) and not isBadVersion(middle - 1):
                return middle
            else:
                end = middle - 1
        return 0