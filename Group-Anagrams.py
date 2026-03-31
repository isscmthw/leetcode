1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        def getfreqstring(element):
4            freqlist=[0]*26
5            for letter in element:
6                freqlist[ord(letter)-ord('a')]+=1
7            freqstring=[]
8            char='a'
9            for i in freqlist:
10                freqstring.append(char)
11                freqstring.append(str(i))
12                char=chr(ord(char)+1)
13            return "".join(freqstring)
14        d={}
15        for word in strs:
16            key=getfreqstring(word)
17            d.setdefault(key,[]).append(word)
18        return list(d.values())