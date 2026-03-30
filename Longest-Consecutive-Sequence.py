1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        d={}
4        maxlength=0
5        for i in nums:
6            d[i]=False
7        for i in nums:
8            currentlength=1
9            nextnum=i+1
10            prevnum=i-1
11            while nextnum in d and  not d[nextnum]:
12                d[nextnum]=True
13                nextnum+=1
14                currentlength+=1
15            while prevnum in d and not d [prevnum]:
16                d[prevnum]=True
17                prevnum-=1
18                currentlength+=1
19            maxlength=max(currentlength,maxlength)
20        return maxlength