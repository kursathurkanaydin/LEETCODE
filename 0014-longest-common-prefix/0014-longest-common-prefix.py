class Solution:
    def longestCommonPrefix(self, dizi: List[str]) -> str:
        en_uzun=""
        first=dizi[0]
        for i in range(len(first)):
            for x in dizi[1:]:
                if i==len(x):
                    return en_uzun
                if first[i]!=x[i]:
                    return en_uzun
            en_uzun+=first[i]
        return en_uzun