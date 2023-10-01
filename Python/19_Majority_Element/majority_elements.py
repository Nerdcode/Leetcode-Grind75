class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(Counter(nums), key=Counter(nums).get)
