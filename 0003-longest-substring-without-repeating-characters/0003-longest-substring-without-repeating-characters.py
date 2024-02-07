from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        adj=defaultdict(int)
        ilk=s[0]
        adj[ilk]=0
        ilk=0
        son=0
        res=0
        for i in range(1,len(s)):
            uzunluk=(son-ilk)+1
            if uzunluk>res:
                res=uzunluk
            harf=s[i]
            if harf in adj and adj[harf]>=ilk:
                ilk=adj[harf]+1
                son=i
                adj[harf]=i
            else:
                adj[harf]=i
                son=i
        uzunluk=(son-ilk)+1
        if uzunluk>res:
            res=uzunluk
        return res