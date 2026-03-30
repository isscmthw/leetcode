1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if not nums:
4            return 0 
5        nums.sort()
6        p1=0
7        length=1
8        maxlength=1
9        while p1<len(nums)-1:
10            if nums[p1+1]==nums[p1]:
11                p1+=1
12            elif nums[p1+1]==nums[p1]+1:
13                length+=1
14                p1+=1
15                if length>maxlength:
16                    maxlength=length
17            else:
18                length=1
19                p1+=1 
20        return maxlength