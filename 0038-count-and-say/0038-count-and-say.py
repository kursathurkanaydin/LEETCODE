class Solution:
    def countAndSay(self, n: int) -> str:
        def kontrol(n):
            if n==1:
                return "1"
            before=kontrol(n-1)
            onceki=before[0]
            count=1
            metin=""
            for i in before[1:]:
                if i ==onceki:
                    count+=1
                else:
                    metin+=str(count)
                    metin+=onceki
                    count=1
                    onceki=i
            metin+=str(count)
            metin+=onceki

            return metin
        return kontrol(n)

