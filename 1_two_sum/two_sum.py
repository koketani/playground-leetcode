from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rev = {}
        for k, v in enumerate(nums):
            rev[v] = k
        for k, v in enumerate(nums):
            kk = rev.get(target-v)
            if not kk or k == kk:
                continue
            return [k, kk]
        return [-1, -1]
