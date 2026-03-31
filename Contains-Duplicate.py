1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        x=set()
4        for i in nums:
5            x.add(i)
6        if len(x)==len(nums):
7            return False
8        else:
9            return True
10            