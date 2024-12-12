class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, v in enumerate(nums):
            ans = target - v
            if ans in seen:
                return [seen[ans], i]
            seen[v] = i



