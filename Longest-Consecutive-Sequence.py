1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        a=0
4        maxlength=0
5        while a<len(nums):
6            length=1
7            currentnumber=nums[a]
8            #this means the same as for i in nums if i+1 in nums which is two loops and if I in nums is O(n)
9            while currentnumber+1 in nums:
10                currentnumber+=1
11                length+=1
12            if length>maxlength:
13                maxlength=length
14            a+=1
15        return maxlength