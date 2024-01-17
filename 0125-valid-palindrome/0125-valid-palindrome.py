class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalnum()])
        temp=[str(a) for a in s]
        start=0
        end=len(s)-1
        while(start<end):
            son=s[end]
            ilk=s[start]
            temp[end]=ilk
            temp[start]=son
            start+=1
            end-=1
        temp="".join([i for i in temp])
        if(temp==s):
            return True
        else:
            return False



