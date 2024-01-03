class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s
        harfler=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        if(len(s)<2):
            return True
        else:
            res=str()
            res2=str()

            for i in s:
                i=i.lower()
                if i in harfler:
                    res+=i
            for b in s[::-1]:
                b=b.lower()
                if b in harfler:
                    res2+=b
            print(res)
            print(res2)
            if(res==res2):
                return True
            else:
                return False
