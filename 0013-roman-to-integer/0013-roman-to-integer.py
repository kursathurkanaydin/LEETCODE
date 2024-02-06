class Solution:
    def romanToInt(self, s: str) -> int:
        numbers={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        """onceki=s[0]
        count=1
        res=0
        for i in range(1,len(s)):
            deger_onceki=numbers[onceki]
            deger_guncel=numbers[s[i]]
            if numbers[onceki]"""
        miktar=0
        total=0
        i=0
        while i<len(s)-1:
            ilk=numbers[s[i]]
            sonraki=numbers[s[i+1]]
            if ilk<sonraki:
                total+=(sonraki-ilk)
                i+=2
                miktar+=2
            else:
                i+=1
                total+=ilk
                miktar+=1
        if miktar<len(s):
            total+=numbers[s[-1]]
        return total