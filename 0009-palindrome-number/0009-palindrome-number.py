class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x<0):
            return False
        else:
            a=list(map(int,str(x)))
            if(a==a[::-1]):
                return True
            else:
                return False