1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        d={}
4        for index,value in enumerate(nums):
5            if target-value in d:
6                return index,d[target-value]
7            else:
8                d[value]=index