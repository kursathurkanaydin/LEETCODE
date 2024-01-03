class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[str(a) for a in s]
        s2=[str(b) for b in t]
        s1.sort()
        s2.sort()
        if(s1==s2):
            return True
        else:
            return False