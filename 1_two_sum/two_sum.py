from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first in enumerate(nums):
            for j, second in enumerate(nums):
                if i >= j:
                    continue
                if first + second == target:
                    return [i, j]
