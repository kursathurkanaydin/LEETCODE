class Solution:
    def isValid(self, s: str) -> bool:
        kontrol ="()[]{}"
        res=[]

        for i in s:
            if(len(res)==0):
                res.append(i)
            else:
                metin="".join(res[-1]+i)
                if(metin in kontrol):
                    res.pop()
                else:
                    res.append(i)
        if(len(res)==0):
            return True
        else:
            return False
    
    