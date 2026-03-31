1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        d={}
4        l=[]
5        for word in strs:
6            key="".join(sorted(word))
7            if key not in d:
8                d[key]=[word]
9            else:
10                d[key].append(word)
11        return list(d.values())
12